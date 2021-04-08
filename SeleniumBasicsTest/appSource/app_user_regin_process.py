from libCommon.selenium_helper import SeleniumHelper
from selenium.webdriver.support.select import Select



class APPUserRegProcess:

    def __init__(self):
        self.url = " http://automationpractice.com/index.php"
        self.helper = SeleniumHelper()

    def launch_app_urp(self):
        self.helper.launch_app(self.url)
        return True

    def user_reg_pro(self):
        self.helper.driver.implicitly_wait(10)
        login = self.helper.driver.find_element_by_class_name("login").click()
        email = self.helper.driver.find_element_by_id("email_create").send_keys("giri123@gmail.com")
        create_acc = self.helper.driver.find_element_by_xpath("//*[@id='SubmitCreate']/span").click()
        self.helper.driver.implicitly_wait(100)
        self.helper.driver.maximize_window()
        gen = self.helper.driver.find_element_by_id("id_gender1").click()
        fname = self.helper.driver.find_element_by_id("customer_firstname").send_keys("Atchyut")
        lname = self.helper.driver.find_element_by_id("customer_lastname").send_keys("Ejjagiri")
        password = self.helper.driver.find_element_by_id("passwd").send_keys("Samata@47")
        drp_days = Select(self.helper.driver.find_element_by_id("days"))
        drp_days.select_by_visible_text("16  ")
        drp_month = Select(self.helper.driver.find_element_by_id("months"))
        drp_month.select_by_visible_text("June ")
        drp_year = Select(self.helper.driver.find_element_by_id("years"))
        drp_year.select_by_visible_text("1990  ")
        fname1 = self.helper.driver.find_element_by_id("firstname").send_keys("Atchyut")
        lanme1 = self.helper.driver.find_element_by_id("lastname").send_keys("Ejjagiri")
        com = self.helper.driver.find_element_by_id("company").send_keys("Mobile")
        address = self.helper.driver.find_element_by_id("address1").send_keys("s/o Moodo kasaiah,Jallapalem road,kondapi")
        add2 = self.helper.driver.find_element_by_id("address2").send_keys("pincode:523270")
        city = self.helper.driver.find_element_by_id("city").send_keys("Ongole")
        drp_state = Select(self.helper.driver.find_element_by_id("id_state"))
        drp_state.select_by_visible_text("Indiana")
        post = self.helper.driver.find_element_by_id("postcode").send_keys("10001")
        coutry = Select(self.helper.driver.find_element_by_id("id_country"))
        coutry.select_by_visible_text("United States")
        cell = self.helper.driver.find_element_by_id("phone_mobile").send_keys("9640100299")
        alis = self.helper.driver.find_element_by_id("alias").send_keys("kumar atchyut")
        btn = self.helper.driver.find_element_by_xpath("//*[@id='submitAccount']/span").click()
        return True



    def val_user(self):
        login = self.helper.driver.find_element_by_class_name("login").click()
        self.helper.driver.implicitly_wait(20)
        mail = self.helper.driver.find_element_by_id("email").send_keys("giri123@gmail.com")
        password = self.helper.driver.find_element_by_id("passwd").send_keys("Samata@47")
        login = self.helper.driver.find_element_by_id("SubmitLogin").click()
        tag = self.helper.driver.find_element_by_tag_name("h1").text
        if tag == "MY ACCOUNT":
            return True
        else:
            raise Exception("invalid user")

    def ver_invalid_email(self):
        login = self.helper.driver.find_element_by_class_name("login").click()
        self.helper.driver.implicitly_wait(5)
        mail = self.helper.driver.find_element_by_id("email").send_keys("ea@gmail.com")
        password =self.helper.driver.find_element_by_id("passwd").send_keys("Samata@47")
        login = self.helper.driver.find_element_by_id("SubmitLogin").click()
        tag = self.helper.driver.find_element_by_tag_name("h1").text
        if not tag == "MY ACCOUNT":
            return True
        else:
            raise Exception("fail to valid email and password")

    def ver_manditary_error(self):
        try:
            self.helper.driver.implicitly_wait(20)
            login = self.helper.driver.find_element_by_class_name("login").click()
            email = self.helper.driver.find_element_by_id("email_create").send_keys("ak234@gmail.com")
            create_acc = self.helper.driver.find_element_by_xpath("//*[@id='SubmitCreate']/span").click()
            gen = self.helper.driver.find_element_by_id("id_gender1").click()
            drp_days = Select(self.helper.driver.find_element_by_id("days"))
            drp_days.select_by_visible_text("16  ")
            drp_month = Select(self.helper.driver.find_element_by_id("months"))
            drp_month.select_by_visible_text("June ")
            drp_year = Select(self.helper.driver.find_element_by_id("years"))
            drp_year.select_by_visible_text("1990  ")
            address = self.helper.driver.find_element_by_id("address1").send_keys("s/o Moodo kasaiah,Jallapalem road,kondapi")
            btn = self.helper.driver.find_element_by_xpath("//*[@id='submitAccount']/span").click()
            return True
        except:
            raise Exception("failed filled mandatory fields")

    def ver_incorrect_data(self):
        try:
            self.helper.driver.implicitly_wait(20)
            login = self.helper.driver.find_element_by_class_name("login").click()
            email = self.helper.driver.find_element_by_id("email_create").send_keys("ak11234@gmail.com")
            create_acc = self.helper.driver.find_element_by_xpath("//*[@id='SubmitCreate']/span").click()
            add2 = self.helper.driver.find_element_by_id("address2").send_keys("pincode:523270")
            btn = self.helper.driver.find_element_by_xpath("//*[@id='submitAccount']/span").click()
        except:
            raise Exception("failed to correct data")
        else:
            return True

if __name__=="__main__":
    obj = APPUserRegProcess()
    obj.launch_app_urp()
    a=obj.user_reg_pro()
    print(a)