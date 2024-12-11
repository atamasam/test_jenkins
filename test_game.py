import unittest
from unittest.mock import patch
import random
from game import guess_number

class TestGame(unittest.TestCase):

    @patch("builtins.input", side_effect=["5"])  # Mock the user input
    @patch("random.randint", return_value=5)     # Mock the random number
    def test_guess_number(self, mock_randint, mock_input):
        # Test that the player guesses the correct number
        result = guess_number()  # Call the function being tested
        self.assertTrue(result)  # Verify that the function returns True when the guess is correct
        mock_randint.assert_called_once_with(1, 10)  # Check that random.randint was called correctly

    @patch("builtins.input", side_effect=["1", "2", "3"])  # Mock the user input
    @patch("random.randint", return_value=5)              # Mock the random number
    def test_guess_number_fail(self, mock_randint, mock_input):
        # Test that the player fails to guess the correct number
        result = guess_number()  # Call the function being tested
        self.assertFalse(result)  # Verify that the function returns False when all guesses are incorrect
        mock_randint.assert_called_once_with(1, 10)  # Check that random.randint was called correctly

if __name__ == "__main__":
    unittest.main()