from selenium import webdriver
from selenium.webdriver.support.ui import Select


class SeleniumBasic:

    def __init__(self):
        # Driver relative path
        self.driver = None
        #self.driver_path = "..\\dependecies\\drivers\\Chrome\\chromedriver.exe"
        self.initialize_driver()

    def initialize_driver(self):
        try:
            self.driver = webdriver.Chrome()
        except:
            print("Initialize driver failed")
        return self.driver

    def close(self):
        self.driver.close()

    def max_window(self):
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def get_cur_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def implecit_waits(self,para):
        self.driver.implicitly_wait(para)

    def Select(self, driver):
        return Select(driver)





