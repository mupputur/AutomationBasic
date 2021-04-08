from libCommon.selenium_helper import SeleniumHelper
from selenium import webdriver


class APPEcAmazonAss1:

    def __init__(self):
        self.url = "https://www.amazon.in/"
        self.helper = SeleniumHelper()

    def launch(self):
        self.helper.launch_app(self.url)
        return True
    
    def user_reg(self):
        try:
            login = self.helper.driver.find_element_by_id("nav-link-accountList").click()
            cre_account = self.helper.driver.find_element_by_id("createAccountSubmit").click()
            name = self.helper.driver.find_element_by_id("ap_customer_name").send_keys("Giri")
            cellno = self.helper.driver.find_element_by_id("ap_phone_number").send_keys("7981083761")
            email=self.helper.driver.find_element_by_id("ap_email").send_keys("atchyute.ds@gmail.com")
            passwd = self.helper.driver.find_element_by_id("ap_password").send_keys("Giri@47")
            conti = self.helper.driver.find_element_by_id("continue").click()
        except:
            raise Exception("failed user registration")
        else:
            return True

    def var_invalid_mobile_number(self):
        try:
            login = self.helper.driver.find_element_by_id("nav-link-accountList").click()
            cre_account = self.helper.driver.find_element_by_id("createAccountSubmit").click()
            name = self.helper.driver.find_element_by_id("ap_customer_name").send_keys("Giri")
            cellno = self.helper.driver.find_element_by_id("ap_phone_number").send_keys("798")
            passwd = self.helper.driver.find_element_by_id("ap_password").send_keys("Giri@47")
            conti = self.helper.driver.find_element_by_id("continue").click()

        except:
            raise Exception("Please provide valid mobile number")
        else:

            return True
    def var_textboxs(self):
        try:
            login = self.helper.driver.find_element_by_id("nav-link-accountList").click()
            cre_account = self.helper.driver.find_element_by_id("createAccountSubmit").click()
            cellno = self.helper.driver.find_element_by_id("ap_phone_number").send_keys("7981254321")

            conti = self.helper.driver.find_element_by_id("continue").click()
            alert_name = self.helper.driver.find_element_by_id("auth-customerName-missing-alert").text
            alert_pass = self.helper.driver.find_element_by_id("auth-password-missing-alert").text

            print(f"name={alert_name} pass ={alert_pass} ")
        except:
            raise Exception("please enter text fields")
        else:
            return alert_name,alert_pass

    def close(self):
        self.helper.close()

if __name__=="__main__":
    obj =APPEcAmazonAss1()
   # obj.launch()
    #obj.var_invalid_mobile_number()
    #obj.var_textboxs()
    # passwd = self.helper.driver.find_element_by_id("ap_password").send_keys("abc")
    # alert_pass_6 =self.helper.driver.find_element_by_class_name("a-alert-content").text
    # alert_cellno = self.helper.driver.find_element_by_class_name("a-list-item").text
    # print(alert_cellno)
    #obj.close()



