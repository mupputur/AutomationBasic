from selenium import webdriver


class SeleniumBasic:

    def __init__(self):
        # Driver relative path
        self.driver = None
        self.driver_path = "..\\dependecies\\drivers\\Chrome\\chromedriver.exe"
        self.initialize_driver()

    def initialize_driver(self):
        try:
            self.driver = webdriver.Chrome(self.driver_path)
        except:
            print("Initilize driver failed")
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
