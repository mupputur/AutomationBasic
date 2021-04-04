from appSource.app_tecklist import APPTechList
import unittest


class TestAPPTechListTask1(unittest.TestCase):

    def setUp(self) -> None:
        self.app = APPTechList()
        print(self._testMethodName)
        self.response = self.app.fill_form()

    def test1_filling_form(self):
        """
        1 Open this link - https://www.techlistic.com/p/selenium-practice-form.html
        2 Enter first and last name (textbox).
        3 Select gender (radio button).
        4 Select years of experience (radio button).
        5 Enter date.
        6 Select Profession (Checkbox).
        7 Select Automation tools you are familiar with (multiple checkboxes).
        8 Select Continent (Select box).
        9 Select multiple commands from a multi select box.
        10 If you can handle Upload image then try it or leave this step.
        11 Click on Download file link and handle the download file pop-up (leave it if you are beginner).
        12 Click on Submit button.

        """
        self.assertTrue(self.response, "Failed to launch application")

    def tearDown(self) -> None:
        self.app.close()


if __name__=="__main__":
    unittest.main()
