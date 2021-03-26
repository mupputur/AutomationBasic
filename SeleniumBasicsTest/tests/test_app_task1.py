from appSource.app_godaddy import APPGoDaddy
import unittest


class TestAPPGoDaddyTask1(unittest.TestCase):

    def setUp(self) -> None:
        self.app=APPGoDaddy()
        print(self._testMethodName)
        self.response = self.app.launch()

    def test1_Launch_browser(self):
        """
        Test Case 1 - Launch browser and Open Godaddy.com Steps to Automate:
                1. Launch browser of your choice say., Firefox, chrome etc.
                2. Open this URL - https://www.godaddy.com/
                3. Close browser.
        """
        self.assertTrue(self.response, "Failed to launch application")

    def test2_max_browser(self):
        """
        Test Case 2 - Open Godaddy.com and maximize browser window.Steps to Automate:
        1. Launch browser of your choice say., Firefox, chrome etc.
        2. Open this URL - https://www.godaddy.com/
        3. Maximize or set size of browser window.
        4. Close browser.
        """
        self.assertTrue(self.response, "Failed to launch an app")
        res_max = self.app.maximize_app()
        self.assertTrue(res_max, "Failed to maximize window")

    def test3_get_title(self):
        """
        Test Case 3 - Open Godaddy.com and Print it's Page title.Steps to Automate:
        1. Launch browser of your choice say., Firefox, chrome etc.
        2. Open this URL - https://www.godaddy.com/
        3. Maximize or set size of browser window.
        4. Get Title of page and print it.
        5. Close browse"""
        expected_title = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy IN"
        self.assertTrue(self.response, "Failed to launch application")
        res_max1 = self.app.maximize_app()
        self.assertTrue(res_max1, "Failed to maximize window")
        res_title = self.app.get_app_properties()[0]
        print("Got Title: {} Expected : {}".format(res_title, expected_title))
        self.assertEqual(expected_title, res_title, "Failed to get a title")

    def test4_get_url(self):
        """

        :return:
        """
        expected_url = "https://in.godaddy.com/"
        self.assertTrue(self.response, "Failed to launch application")
        res_max2 = self.app.maximize_app()
        self.assertTrue(res_max2, "Failed to maximize window")
        res_url = self.app.get_app_properties()[1]
        self.assertTrue(res_url, "Failed to get current url")
        print("Got Title: {} Expected : {}".format(res_url,expected_url))
        self.assertEqual(expected_url, res_url, "Failed to get a url")

    def test5_get_pagesource(self):
        """
        Test Case 5 - Open Godaddy.com and Print Page source.
        Steps to Automate:
        1. Launch browser of your choice say., Firefox, chrome etc.
        2. Open this URL - https://www.godaddy.com/
        3. Maximize or set size of browser window.
        4. Get Page source and print it.
        5. Close browser.

        :return:
        """

        exp_page_tag = "Millions of customers rely on our domains and web hosting to get their ideas online."
        self.assertTrue(self.response, "Failed to launch application")
        res_max2 = self.app.maximize_app()
        self.assertTrue(res_max2, "Failed to maximize window")
        res_page = self.app.get_source()
        self.assertIsNotNone(res_page, "Failed to get page source")

    def test6_properties_validation(self):
        """
        Test Case 6 - Open Godaddy.com and Validate Page Title
        Steps to Automate:
        1. Launch browser of your choice say., Firefox, chrome etc.
        2. Open this URL - https://www.godaddy.com/
        3. Maximize or set size of browser window.
        4. Get Title of page and validate it with expected value.
        5. Get URL of current page and validate it with expected value.
        6. Get Page source of web page.
        7. And Validate that page title is present in page source.
        8. Close browser.

        :return:
        """
        self.assertTrue(self.response, "Failed to launch application")
        res_max2 = self.app.maximize_app()
        self.assertTrue(res_max2, "Failed to maximize window")
        exp_title = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy IN"
        act_title = self.app.get_app_properties()[0]
        self.assertEqual(act_title, exp_title, "Failed to get title")
        exp_url = "https://in.godaddy.com/"
        act_url = self.app.get_app_properties()[1]
        self.assertEqual(act_url, exp_url, "Failed to get url")
        res_page = self.app.get_source()
        self.assertIsNotNone(res_page, "Failed to get page source")

    def tearDown(self) -> None:
        self.app.close()


if __name__=="__main__":
    unittest.main()
