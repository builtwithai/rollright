# Roll Right
Roll Right is an innovative machine learning application designed to enhance accessibility in our everyday environment. Its primary function is to detect and interpret sign language, specifically tailored towards actions such as opening a door. By harnessing the power of machine learning algorithms, Roll Right aims to bridge the communication gap and provide a seamless interaction experience for individuals who use sign language. With Roll Right, command a door to open without physical touch, but through the universal language of signs.

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
To run the code, you need to provide either an image file or a video file as an argument. The code will load the file, preprocess it, and use the TensorFlow Lite model to predict whether the image or the video contains ASL for a door or not. The code will print the predicted label for the file.

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
The TensorFlow Lite model used for the project is `models/model_unquant.tflite`. The model was trained using https://teachablemachine.withgoogle.com/


## License
The project and the model are licensed under the MIT License. See the `LICENSE` file for more details.

## Credits
The project and the model were created by the following authors and contributors:

