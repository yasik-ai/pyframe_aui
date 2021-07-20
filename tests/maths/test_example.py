""" Create All Your Tests Here """
import pytest
from pytest import mark
from commonutils.fileUtils import FileUtils

@mark.smokeClass
class Tests_examples:
    @mark.smoke
    def test_addition(self):
        assert 1 + 1 == 2


    @mark.smoke
    @mark.regression
    def test_subtraction(self):
        diff = 1 - 1
        assert diff == 0


    # def test_dumm(self):
    #     assert True

    def test_files(self):
     assert True


