from unittest import TestCase

from polygon import Polygon


class TestPolygon(TestCase):
    def test_get_perimeter(self):
        # arrange
        expected_side_length_0 = 3
        expected_side_length_1 = 4
        expected_side_length_2 = 5
        expected_perimeter = 12
        expected_number_of_sides = 3
        triangle = Polygon("", expected_number_of_sides)
        triangle.set_side_length(0, expected_side_length_0)
        triangle.set_side_length(1, expected_side_length_1)
        triangle.set_side_length(2, expected_side_length_2)

        # act
        actual_side_length_0 = triangle.get_side_length(0)
        actual_side_length_1 = triangle.get_side_length(1)
        actual_side_length_2 = triangle.get_side_length(2)
        actual_perimeter = triangle.get_perimeter()
        actual_number_of_sides = triangle.get_number_of_sides()

        # assert
        self.assertEqual(expected_side_length_0, actual_side_length_0)
        self.assertEqual(expected_side_length_1, actual_side_length_1)
        self.assertEqual(expected_side_length_2, actual_side_length_2)
        self.assertEqual(expected_perimeter, actual_perimeter)
        self.assertEqual(expected_number_of_sides, actual_number_of_sides)
