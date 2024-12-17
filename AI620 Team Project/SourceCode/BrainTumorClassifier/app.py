from chalice import Chalice, Response
import boto3
import os
import numpy as np
from PIL import Image
import io
import tensorflow.lite as tflite  # Use tflite-runtime

# App initialization
app = Chalice(app_name='brain-tumor-classifier')

# Constants
BUCKET_NAME = "ai620-suichenglai"  # Replace with your S3 bucket
MODEL_KEY = "model/brain_tumor_classifier.tflite"  # Path to your TFLite model in S3
IMAGE_SIZE = 224  # Input image size
CLASS_NAMES = ["Glioma", "Healthy", "Meningioma", "Pituitary"]  # Adjust based on your model
LOCAL_MODEL_DIR = "/tmp"  # Chalice allows write access only to '/tmp'
LOCAL_MODEL_PATH = os.path.join(LOCAL_MODEL_DIR, "brain_tumor_classifier.tflite")

# Global variable for the model to cache it
interpreter = None


# Function to download the TFLite model from S3 and load it
def load_model_from_s3():
    global interpreter
    if interpreter is None:  # Load the model only once
        s3 = boto3.client("s3")

        # Download the model if it does not exist locally
        if not os.path.exists(LOCAL_MODEL_PATH):
            print(f"Downloading model from S3 bucket: {BUCKET_NAME}")
            s3.download_file(BUCKET_NAME, MODEL_KEY, LOCAL_MODEL_PATH)
            print("Model downloaded successfully.")

        # Load the TFLite model using the TensorFlow Lite interpreter
        print("Loading TFLite model...")
        interpreter = tflite.Interpreter(model_path=LOCAL_MODEL_PATH)
        interpreter.allocate_tensors()
        print("Model loaded successfully.")
    return interpreter


# Function to preprocess the input image
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))  # Resize image
    image_array = np.array(image) / 255.0  # Normalize pixel values
    return np.expand_dims(image_array, axis=0)  # Add batch dimension


# Function to perform prediction using the TFLite model
def predict(image_bytes):
    # Load the model
    interpreter = load_model_from_s3()

    # Preprocess image
    input_data = preprocess_image(image_bytes)

    # Get input and output tensor indices
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Set the input tensor to the image
    interpreter.set_tensor(input_details[0]['index'], input_data.astype(np.float32))

    # Run inference
    interpreter.invoke()

    # Get prediction results
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class = np.argmax(output_data, axis=1)[0]
    confidence = float(np.max(output_data))

    return {
        "predicted_class": CLASS_NAMES[predicted_class],
        "confidence": confidence
    }


# Route for the root endpoint
@app.route("/", methods=["GET"])
def index():
    return Response(
        body={"message": "Welcome to the Brain Tumor Classifier API! Use POST /predict to upload an image."},
        status_code=200,
        headers={"Content-Type": "application/json"}
    )


# Route to handle image uploads and make predictions

#@app.route("/predict", methods=["POST"], cors=True)  # use this line for local testing index-local.html against local deployment by 'chalice local'
@app.route("/predict", methods=["POST"], cors=True)   # use this line for testing index.html against cloud deployment by 'chalice deploy'

def predict_route():
    # Check if the request has a body
    request = app.current_request
    if not request.raw_body:
        return Response(
            body={"error": "No image provided in the request body."},
            status_code=400,
            headers={"Content-Type": "application/json"}
        )

    try:
        # Read the uploaded image
        image_bytes = request.raw_body

        # Perform prediction
        prediction = predict(image_bytes)

        # Return the prediction as a JSON response
        return Response(
            body=prediction,
            status_code=200,
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        # Handle any errors during prediction
        return Response(
            body={"error": str(e)},
            status_code=500,
            headers={"Content-Type": "application/json"}
        )
