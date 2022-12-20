import unittest
from pytest import raises
from files import *

class TestClass:
    """ Test """

    def test_files_no_path(self):
        """ Test"""
        with raises(FileNotFoundError):
         readfile('')
    
    def test_files_wrong_path(self):
        """ Test"""
        with raises(FileNotFoundError):
         readfile('months.txt')
         
    def test_files_correct_path(self):
        """ Test"""
        assert readfile('code/files/files/months.txt') == "January\n"

 

if __name__ == '__main__':
    unittest.main()