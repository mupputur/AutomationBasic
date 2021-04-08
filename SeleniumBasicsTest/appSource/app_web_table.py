from libCommon.selenium_helper import SeleniumHelper
import time

class AppWebTable:

    def __init__(self):
        self.helper = SeleniumHelper()
        self.driver = self.helper.initialize_driver()

    def lanch_app(self):
        url ="https://www.w3schools.com/html/html_tables.asp"
        self.helper.launch_app(url)

    def web_table(self):
        rows = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        cols =len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))
        print("company"+"            "+"contact"+"         "+"country")
        for r in range(2,rows+1):
            for c in range(1,cols+1):
                value =self.driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                print(value, end='  ')
            print()


if __name__ == "__main__":
    a11 = AppWebTable()
    a11.lanch_app()
    a11.web_table()
