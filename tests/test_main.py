import unittest
import sys
import cv2
import sys

sys.path.append('app')

from main import predict_label  
from main import predict_label_from_video

class TestPredictLabel(unittest.TestCase):
    def test_predict_label_door(self):
        # Use a known image for the test
        image_path = 'tests/testdoor.jpeg'

        # Call the function with the test image
        result = predict_label(image_path)
        print(f"Predicted label for {image_path}: {result}")

        # Check that the result is as expected
        # This will depend on what your function returns
        # For example, if it returns a label, you might check that the label is correct
        self.assertEqual(result, 'Open Door')

    def test_predict_label_not_door(self):
        # Use a known image for the test
        image_path = 'tests/testnotdoor.jpeg'

        # Call the function with the test image
        result = predict_label(image_path)
        print(f"Predicted label for {image_path}: {result}")

        # Check that the result is as expected
        # This will depend on what your function returns
        # For example, if it returns a label, you might check that the label is correct
        self.assertEqual(result, 'Other Sign')
    
    def test_predict_label_from_video(self):
        # Use a known image for the test
        video_file_path = 'tests/test.mp4'
        result=predict_label_from_video(video_file_path)
        print(f"Predicted label for {video_file_path}: {result}")

        # Check that the result is as expected
        # This will depend on what your function returns
        # For example, if it returns a label, you might check that the label is correct
        self.assertEqual(result, 'Open Door')



if __name__ == '__main__':
    unittest.main()       
