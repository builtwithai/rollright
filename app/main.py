import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import os
import glob

# Path to the TensorFlow Lite model file
tflite_model_path = 'models/model_unquant.tflite'

# Load the TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load and preprocess image
def load_and_preprocess_image(image_path):
    print(f"image_path: {image_path}")
    image = Image.open(image_path)
    image = image.resize((input_details[0]['shape'][2], input_details[0]['shape'][1]))
    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Create labels
def create_labels():
    labels = np.array(["Open Door", "Other Sign"])
    return labels

labels = create_labels()


def predict(image):
    """
    Predicts the label for an image.

    Args:
        image (numpy.ndarray): The image array to be predicted.

    Returns:
        numpy.ndarray: The predicted label for the image.
    """
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data


# Predict label for an image file

def predict_label(image_path):
    """
    Predicts the label for an image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The predicted label for the image.
    """
    image = load_and_preprocess_image(image_path)
    result = predict(image)
    predicted_class_index = np.argmax(result)
    predicted_class_label = labels[predicted_class_index]
    return predicted_class_label


# Preprocess image for model input
def preprocess(image):
    if len(input_details[0]['shape']) < 3:
        print("Error: The model's input shape is invalid.")
        return
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    if height <= 0 or width <= 0:
        print("Error: The model's input height and width are invalid.")
        return
    image = cv2.resize(image, (width, height))
    image_array = np.array(image, dtype=np.float32) / 255.0
    return image_array

# Predict label for each frame in a video
def predict_label_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video")
        return
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            processed_frame = preprocess(frame)
            input = np.expand_dims(processed_frame, axis=0)
            prediction = predict(input)
            index = np.argmax(prediction)
            predicted_class_label = labels[index]
            # print(f"Predicted label for frame: {predicted_class_label}")
        else:
            break
    cap.release()
    cv2.destroyAllWindows
    return predicted_class_label


