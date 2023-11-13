import unittest
import sys
sys.path.append('app')

from main import predict_label  # replace with your actual module

class TestPredictLabel(unittest.TestCase):
    def test_predict_label_door(self):
        # Use a known image for the test
        image_path = 'tests/testdoor.jpeg'

        # Call the function with the test image
        result = predict_label(image_path)
        print("result: ", result)

        # Check that the result is as expected
        # This will depend on what your function returns
        # For example, if it returns a label, you might check that the label is correct
        self.assertEqual(result, 'Door')

    def test_predict_label_not_door(self):
        # Use a known image for the test
        image_path = 'tests/testnotdoor.jpeg'

        # Call the function with the test image
        result = predict_label(image_path)

        # Check that the result is as expected
        # This will depend on what your function returns
        # For example, if it returns a label, you might check that the label is correct
        self.assertEqual(result, 'Not Door')

if __name__ == '__main__':
    unittest.main()