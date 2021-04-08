
import unittest,HtmlTestRunner,sys
sys.path.append("C:\\Users\91964\PycharmProjects\SeleniumBasicsTest")
from appSource.app_practice_form import AppPracticeForm


class TestAppPracticeFormTask2(unittest.TestCase):

    def setUp(self) -> None:
        self.app=AppPracticeForm()
        print(self._testMethodName)
        self.response = self.app.launch()

    def test1_Launch_browser(self):
        self.assertTrue(self.response, "Failed to launch application")

    def test2_form_fill(self):
        act_res = self.app.pra_form2()
        self.assertTrue(act_res, "Failed to form fill")

    def tearDown(self) -> None:
        self.app.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\91964\\PycharmProjects\\SeleniumBasicsTest\\Reports"))




