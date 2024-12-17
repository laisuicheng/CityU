import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image

# Load model
interpreter = tflite.Interpreter(model_path="./model/brain_tumor_classifier.tflite")
interpreter.allocate_tensors()

# Prepare input data
image = Image.open("0003.jpg").resize((224, 224))
image_array = np.array(image) / 255.0
input_data = np.expand_dims(image_array, axis=0).astype(np.float32)

# Run inference
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
predicted_class = np.argmax(output_data, axis=1)[0]
print("Prediction:", predicted_class)
