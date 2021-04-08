import HtmlTestRunner as h
import datetime as dt

import unittest
h.__author__="Atchyut kumar"
h.__email__="ejjagiriatchyutkumar@gmail.com"
class Test1(unittest.TestCase):

    def test1(self):
        self.assertTrue(True, "Failed to launch application")
    def test2(self):
        self.assertTrue(True,"failed test2")
if __name__=="__main__":
    unittest.main(testRunner=h.HTMLTestRunner(output= "C:\\Users\\91964\\PycharmProjects\\SeleniumBasicsTest\\Reports"))




