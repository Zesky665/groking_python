import unittest
from calc import *


class TestClass:
    """ Test """

    def test_add(self):
        """ Test """
        assert add(10, 5) == 15
        assert add(-1, 1) == 0
        assert add(-1,-1) == -2

    def test_subtract(self):
        """ Test """
        assert subtract(10, 5) == 5
        assert subtract(-1, 1) == -2
        assert subtract(-1, -1) == 0

    def test_multiply(self):
        """ Test """
        assert multiply(10, 5) == 50
        assert multiply(-1, 1) == -1
        assert multiply(-1, -1) == 1

    def test_divide(self):
        """ Test """
        assert divide(10, 5) == 2
        assert divide(-1, 1) == -1
        assert divide(-1, -1) == 1
        assert divide(5, 2) == 2.5



if __name__ == '__main__':
    unittest.main()