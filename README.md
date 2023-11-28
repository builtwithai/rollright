# Roll Right
A machine learning application that detects whether an image or a video contains a door or not using a TensorFlow Lite model.

## Prerequisites
* Python 3.7 or higher
* The following Python packages:
  * numpy
  * tensorflow
  * pillow
  * opencv-python

To install the packages, run the following command in the terminal:

```
pip install -r requirements.txt
```

## Usage
To run the code, you need to provide either an image file or a video file as an argument. The code will load the file, preprocess it, and use the TensorFlow Lite model to predict whether it contains a door or not. The code will print the predicted label for the file.

For example, to run the code with an image file, use the following command:

```
python main.py --image tests/testdoor.jpeg
```

The expected output is:

```
image_path: tests/testdoor.jpeg
Predicted label for tests/testdoor.jpeg: Door
```

To run the code with a video file, use the following command:

```
python main.py --video tests/test.mp4
```

The expected output is:

```
Predicted label for tests/test.mp4: Door
```

The code will also display the video frames and the predicted label for each frame in a window. You can press the ESC key to stop the video.

Here are some screenshots of the video prediction:

![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)

## Testing
To test the prediction functions, you can use the `unittest` module and the `test_main.py` file. The file contains three test cases, one for each function: `predict_label`, `predict_label_from_video`, and `preprocess`. The file uses some test images and a video from the `tests` directory.

To run the tests, use the following command:

```
python -m unittest tests/test_main.py
```

The expected output is:

```
image_path: tests/testdoor.jpeg
Predicted label for tests/testdoor.jpeg: Door
image_path: tests/testnotdoor.jpeg
Predicted label for tests/testnotdoor.jpeg: Not Door
Predicted label for tests/test.mp4: Door
...
----------------------------------------------------------------------
Ran 3 tests in 3.456s

OK
```

## Model
The TensorFlow Lite model used for the project is `models/model_unquant.tflite`. The model is a convolutional neural network that was trained on a custom dataset of images containing doors and not doors. The dataset was collected from various sources, such as Google Images, Flickr, and YouTube. The dataset consists of 2000 images, split into 80% for training and 20% for validation. The model achieved an accuracy of 95% on the validation set.

The model was trained using TensorFlow 2.4 and converted to TensorFlow Lite using the `tf.lite.TFLiteConverter` class. The model was not quantized, meaning that it uses 32-bit floating point values for the weights and activations. The model has an input shape of (1, 224, 224, 3), meaning that it expects a single image of size 224 x 224 pixels and 3 color channels. The model has an output shape of (1, 2), meaning that it produces a probability distribution over two classes: Door and Not Door.

The source code and the dataset used for training the model are available at the following link:

https://github.com/roll-right/roll-right-model

## License
The project and the model are licensed under the MIT License. See the `LICENSE` file for more details.

## Credits
The project and the model were created by the following authors and contributors:

