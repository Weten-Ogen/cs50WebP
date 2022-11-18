import unittest

from app import square

class Tests(unittest.TestCase):

    def test1(self):
        self.assertTrue(square(10), 100)

    def test2(self):
        self.assertTrue(square(40), 1600)

    def test3(self):
        self.assertFalse(square(1), 2)
    
    def test4(self):
        self.assertFalse(square(2), 4)


if __name__ == "__main__":
    unittest.main()