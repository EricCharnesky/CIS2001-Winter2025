from unittest import TestCase
from infantry import Infantry

class TestInfantry(TestCase):
    def test_move_works(self):

        # arrange
        expected_x_position = 5
        expected_y_position = 0
        infantry = Infantry(0, 0, "")

        # act
        infantry.move(5, 0)
        actual_x_position = infantry.get_x_position()
        actual_y_position = infantry.get_y_position()

        # assert
        self.assertEqual(expected_x_position, actual_x_position)
        self.assertEqual(expected_y_position, actual_y_position)

    def test_move_fails_both_directions(self):

        # arrange
        expected_x_position = 0
        expected_y_position = 0
        infantry = Infantry(0, 0, "")

        # act - https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        self.assertRaises(ValueError, infantry.move, 5, 5)
        actual_x_position = infantry.get_x_position()
        actual_y_position = infantry.get_y_position()

        # assert
        self.assertEqual(expected_x_position, actual_x_position)
        self.assertEqual(expected_y_position, actual_y_position)

    def test_move_fails_more_than_max(self):

        # arrange
        expected_x_position = 0
        expected_y_position = 0
        infantry = Infantry(0, 0, "")

        # act - https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        self.assertRaises(ValueError, infantry.move, 10, 0)
        actual_x_position = infantry.get_x_position()
        actual_y_position = infantry.get_y_position()

        # assert
        self.assertEqual(expected_x_position, actual_x_position)
        self.assertEqual(expected_y_position, actual_y_position)

