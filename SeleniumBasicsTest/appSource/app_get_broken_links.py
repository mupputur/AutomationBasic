import requests
from selenium import webdriver
from libCommon.selenium_helper import SeleniumHelper

class AppGetBrokenLinks:

    def __init__(self):
        self.url = "http://automationpractice.com/index.php"
        self.helper = SeleniumHelper()
    def get_broken_links(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        driver=webdriver.Chrome(chrome_options=options, executable_path=self.helper.driver_path)
        driver.get(self.url)
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            res = requests.head(link.get_attribute('href'))
            #res = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), res.status_code)
if __name__ == "__main__":
    a9 = AppGetBrokenLinks()
    a9.get_broken_links()
