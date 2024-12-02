import unittest
from unittest.mock import patch
import random
from game import guess_number

class TestGame(unittest.TestCase):

    @patch("builtins.input", side_effect=["5"])  # Mocke die Eingabe
    @patch("random.randint", return_value=5)     # Mocke die Zufallszahl
    def test_guess_number(self, mock_randint, mock_input):
        # Teste, dass der Spieler das richtige Ergebnis bekommt
        result = guess_number()
        self.assertTrue(result)
        mock_randint.assert_called_once_with(1, 10)  # Überprüft, dass random.randint korrekt aufgerufen wurde

    @patch("builtins.input", side_effect=["1", "2", "3"])  # Mocke die Eingabe
    @patch("random.randint", return_value=5)                 # Mocke die Zufallszahl
    def test_guess_number_fail(self, mock_randint, mock_input):
        # Teste, dass der Spieler das falsche Ergebnis bekommt
        result = guess_number()
        self.assertFalse(result)
        mock_randint.assert_called_once_with(1, 10)  # Überprüft, dass random.randint korrekt aufgerufen wurde

if __name__ == "__main__":
    unittest.main()