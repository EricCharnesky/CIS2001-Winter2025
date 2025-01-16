from unittest import TestCase

from triangle import Triangle


class TestTriangle(TestCase):
    def test_get_area(self):
        # arrange
        expected_area = 6
        triangle = Triangle("")
        triangle.set_side_length(0, 3)
        triangle.set_side_length(1, 4)
        triangle.set_side_length(2, 5)

        # act
        actual_area = triangle.get_area()

        # assert
        self.assertEqual(expected_area, actual_area)

