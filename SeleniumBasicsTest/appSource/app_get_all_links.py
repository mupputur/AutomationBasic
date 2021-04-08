from libCommon.selenium_helper import SeleniumHelper
import requests

class AppGetLinks:

    def __init__(self):
        self.url = "http://automationpractice.com/index.php"
        self.helper = SeleniumHelper()
        self.driver = self.helper.initialize_driver()

    def open_app(self):
        self.helper.launch_app(self.url)

    def get_links(self):
        links = self.driver.find_elements_by_xpath("//a[@href]")
        for link in links:
            print(link.get_attribute("href"))

    def broken_links(self):
        links = self.driver.find_elements_by_css_selector("a")
        for link in links:
            r = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)

    def close_app(self):
        self.helper.close()

if __name__=="__main__":
    a8 = AppGetLinks()
    a8.open_app()
    #a8.get_links()
    a8.broken_links()
