import unittest
from game import guess_number

class TestGame(unittest.TestCase):
    def test_guess_number(self):
        # Mocke den Zufallswert und Eingaben (z. B. Spieler gewinnt sofort)
        random.seed(1)  # Immer dieselbe Zahl generieren
        with unittest.mock.patch("builtins.input", side_effect=["5"]):
            result = guess_number()
            self.assertTrue(result)

    def test_guess_number_fail(self):
        # Spieler verliert (z. B. falsche Zahlen geraten)
        random.seed(1)
        with unittest.mock.patch("builtins.input", side_effect=["1", "2", "3"]):
            result = guess_number()
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()