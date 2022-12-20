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
        assert readfile('code/files/files/months.txt') == "January"

    def test_files_line_0(self):
        """ Test"""
        assert readline('code/files/files/months.txt', 0) == "January"

    def test_files_line_6(self):
        """ Test"""
        assert readline('code/files/files/months.txt', 5) == "June"
        
    def test_files_line_12(self):
        """ Test"""
        assert readline('code/files/files/months.txt',11) == "December"
 

if __name__ == '__main__':
    unittest.main()