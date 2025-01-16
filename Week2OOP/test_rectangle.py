from lib2to3.btm_utils import rec_test
from unittest import TestCase

from rectangle import Rectangle


class TestRectangle(TestCase):
    def test_get_area(self):
        # arrange
        expected_length = 5
        expected_width = 4
        expected_area = 20
        rectangle = Rectangle("")
        rectangle.set_length(expected_length)
        rectangle.set_width(expected_width)

        # act
        actual_length = rectangle.get_length()
        actual_width = rectangle.get_width()
        actual_area = rectangle.get_area()

        # assert
        self.assertEqual(expected_area, actual_area)
        self.assertEqual(expected_width, actual_width)
        self.assertEqual(expected_length, actual_length)
