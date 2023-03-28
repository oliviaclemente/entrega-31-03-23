import unittest
from ej2 import determinante_sarrus

class TestDeterminanteSarrus(unittest.TestCase):
    def test_determinante_sarrus(self):
        matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        matriz3 = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
        matriz4 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.assertEqual(determinante_sarrus(matriz1), 0)
        self.assertEqual(determinante_sarrus(matriz2), 3)
        self.assertEqual(determinante_sarrus(matriz3), -6)
        self.assertEqual(determinante_sarrus(matriz4), -3)

if __name__ == '__main__':
    unittest.main()
