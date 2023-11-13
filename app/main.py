import numpy as np
import tensorflow as tf
from PIL import Image

# Path to the TensorFlow Lite model file
tflite_model_path = 'models/model_unquant.tflite'

# Load the TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def load_and_preprocess_image(image_path):
    # Load the image
    image = Image.open(image_path).convert('RGB')

    # Resize the image to match the input size of the model
    image = image.resize((input_details[0]['shape'][2], input_details[0]['shape'][1]))

    # Convert to numpy array and normalize
    image_array = np.array(image, dtype=np.float32) / 255.0

    # Add a batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def create_labels():
    labels = np.array(["Door", "Not Door"])
    return labels

labels = create_labels()

def predict(image_path):
    # Preprocess the image
    preprocessed_image = load_and_preprocess_image(image_path)

    # Set the tensor to point to the input data to be inferred
    interpreter.set_tensor(input_details[0]['index'], preprocessed_image)

    # Run the inference
    interpreter.invoke()

    # Extract the output
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

# Example usage
import os
import glob

def predict_label(image_path):
    result = predict(image_path)
    predicted_class_index = np.argmax(result)
    predicted_class_label = labels[predicted_class_index]
    print(f"Predicted label for {image_path}: {predicted_class_label}")
    return predicted_class_label

# Specify the directory
directory = 'data/'

# Get a list of all image paths in the directory
image_paths = glob.glob(os.path.join(directory, '*.jpeg'))

for image_path in image_paths:
    predict_label(image_path)