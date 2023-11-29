# Roll Right
Roll Right is an innovative machine learning application designed to enhance accessibility in our everyday environment. Its primary function is to detect and interpret sign language, specifically tailored towards actions such as opening a door. By harnessing the power of machine learning algorithms, Roll Right aims to bridge the communication gap and provide a seamless interaction experience for individuals who use sign language. With Roll Right, command a door to open without physical touch, but through the universal language of signs.

---
## Hardware
The following components are required for this project:
1. [Coral Dev Board Micro](https://coral.ai/docs/dev-board-micro/get-started/)
2. USB 2.0 to TTL Module Serial Converter Adapter
3. USB-C Power Supply
4. [Coral Camera Module](https://coral.ai/docs/camera/datasheet) or webcam feed
---

## Setup Coral Dev Board Micro
1. Follow the [Getting Started Guide](https://coral.ai/docs/dev-board-micro/get-started/) to setup the Coral Dev Board Micro for the platform you are using.
2. Connect the Coral Camera Module to the Coral Dev Board Micro
3. Connect the USB 2.0 to TTL Module Serial Converter Adapter to the Coral Dev Board Micro
4. Connect the USB-C Power Supply to the Coral Dev Board Micro

## Connect to the Coral Dev Board Micro
```bash
screen /dev/cu.usbserial-0001 115200
```

## Flash Coral Dev Board before running the project
```bash

```

## Software
The following software is required for this project:

## Prerequisites
* Python 3.7 or higher
* The following Python packages:
  * numpy
  * tensorflow
  * pillow
  * opencv-python




To install the packages, run the following command in the terminal:

```
gh repo clone builtwithai/rollright
cd rollright
pip install -r requirements.txt
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
Predicted label for tests/testdoor.jpeg: Open Door
image_path: tests/testnotdoor.jpeg
Predicted label for tests/testnotdoor.jpeg: Other Sign
Predicted label for tests/test.mp4: Open Door
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

