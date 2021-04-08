from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from libCommon.selenium_helper import SeleniumHelper
from selenium import webdriver


class AppEcAmazonAss2:

    def __init__(self):

        #driver_path = "..\\dependecies\\drivers\\Chrome\\chromedriver.exe"
        #self.driver = webdriver.Chrome(driver_path)
        self.help = SeleniumHelper()
        url = "https://www.amazon.in/"
        self.help.driver.get(url)
    '''
    def open_app(self):
        self.help.driver.get(self.url)
        return True

    def user_login(self):
        try:
            login = self.help.wait.until(ec.presence_of_element_located((By.ID, "nav-link-accountList")))
            login.click()
            cellno = self.help.wait.until(ec.presence_of_element_located((By.ID, "ap_email")))
            cellno.send_keys("7981083761")
            self.help.driver.find_element_by_id("continue").click()
            passwd = self.help.wait.until(ec.presence_of_element_located((By.ID, "ap_password")))
            passwd.send_keys("Giri@47")
            self.help.driver.find_element_by_id("signInSubmit").click()
        except:
            raise Exception("user login fail")
        else:
            return True'''

    def buy_product(self):
        search = self.help.driver.find_element_by_id("twotabsearchtextbox").send_keys("laptop power cable")
        self.help.driver.find_element_by_id("nav-search-submit-text").click()
        brand1 = self.help.wait.until(ec.presence_of_element_located((By.ID, "p_89/DAHSHA"))).click()
        #brand2 = self.help.wait.until(ec.presence_of_element_located((By.ID, "p_89/Storite"))).click()
        price_range = self.help.wait.until(ec.presence_of_element_located((By.ID, "p_36/1318503031"))).click()
        discount = self.help.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "a-size-base a-color-base"))).click()
        item = self.help.driver.find_element_by_class_name("a-section aok-relative s-image-square-aspect").click()







    ''''
    def close_app(self):
        self.help.close()'''

if __name__ == "__main__":
    a2 =AppEcAmazonAss2()
    #a2.open_app()
    #a2.user_login()
    #a2.close_app()
    a2.buy_product()