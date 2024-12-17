from chalice import Chalice, Response
import boto3
import os
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax

# Load the Keras model
model=load_model('brain_tumor_classifier.keras', custom_objects={"softmax_v2": softmax})
#model = tf.keras.models.load_model('brain_tumor_classifier.keras')

# Convert the model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open('brain_tumor_classifier.tflite', 'wb') as f:
    f.write(tflite_model)