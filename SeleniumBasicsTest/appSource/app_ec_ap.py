from libCommon.selenium_helper import SeleniumHelper
from selenium.webdriver.common.action_chains import ActionChains
import time


class AppEcAp:

    def __init__(self):
        self.helper = SeleniumHelper()
        self.driver =self.helper.initialize_driver()

    def open_app(self):
        url = "http://automationpractice.com/index.php"
        self.helper.launch_app(url)

    def user_login(self):
        self.driver.implicitly_wait(10)
        login = self.driver.find_element_by_class_name("login").click()
        email = self.driver.find_element_by_id("email").send_keys("eak403@gmail.com")
        passwd = self.driver.find_element_by_id("passwd").send_keys("Samata@47")
        sign_in = self.driver.find_element_by_id("SubmitLogin").click()

    def var_empty_fields_signin(self):
        login = self.driver.find_element_by_class_name("login").click()
        sign_in = self.driver.find_element_by_id("SubmitLogin").click()
        error = self.driver.find_element_by_xpath("//*[@id='center_column']/div[1]").text
        print(error)

    def var_email(self):
        login = self.driver.find_element_by_class_name("login").click()
        email = self.driver.find_element_by_id("email").send_keys("ea1235@gmail.com")
        sign_in = self.driver.find_element_by_id("SubmitLogin").click()
        error = self.driver.find_element_by_xpath("//*[@id='center_column']/div[1]").text
        print(error)

    def var_pass(self):
        login = self.driver.find_element_by_class_name("login").click()
        passwd = self.driver.find_element_by_id("passwd").send_keys("Samata@47")
        sign_in = self.driver.find_element_by_id("SubmitLogin").click()
        error = self.driver.find_element_by_xpath("//*[@id='center_column']/div[1]").text
        print(error)

    def var_both(self):
        login = self.driver.find_element_by_class_name("login").click()
        email = self.driver.find_element_by_id("email").send_keys("eak403@gmail.com")
        passwd = self.driver.find_element_by_id("passwd").send_keys("Samat")#wrong password
        sign_in = self.driver.find_element_by_id("SubmitLogin").click()
        error = self.driver.find_element_by_xpath("//*[@id='center_column']/div[1]").text
        print(error)

    def move_ele(self):
        try:
            women = self.driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a")
            t_shirt = self.driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/ul/li[1]/ul/li[1]/a")
            actions = ActionChains(self.driver)
            actions.move_to_element(women).move_to_element(t_shirt).click().perform()
            pro_name = self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li/div/div[2]/h5/a").text
            print(pro_name)
            search = self.driver.find_element_by_id("search_query_top").send_keys("Faded Short Sleeve T-shirts")
            click = self.driver.find_element_by_name("submit_search").click()
            after_pro_name = self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li/div/div[2]/h5/a").text
            if pro_name == after_pro_name:
                print("products same")
            else:
                print("products not same")
        except:
            raise Exception("failed to identify product")
        else:
            return True












if __name__=="__main__":
    a = AppEcAp()
    a.open_app()
    #a.var_empty_fields_signin()
    #a.var_email()
    #a.var_pass()
    a.var_both()

    #a.user_login()
    #a.move_ele()
