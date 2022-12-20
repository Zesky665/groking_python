import unittest
from greet import *

class TestClass:
    """ Test """

    def test_greet(self):
        """ Test """
        assert greet() == "Hello Hiring Manager!"
        assert greet('MS.Pearson') == "Hello MS.Pearson!"
        assert greet('!@#') == "Hello !@#!"


if __name__ == '__main__':
    unittest.main()