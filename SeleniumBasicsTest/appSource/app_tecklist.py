from selenium.webdriver.support.select import Select

from libCommon.selenium_helper import SeleniumHelper
import time
from sourcelocators.techlocators import Techlistlocators

class APPTechList:

    def __init__(self):
        self.url = "https://www.techlistic.com/p/selenium-practice-form.html"
        self.driver = SeleniumHelper()
        self.driver.implecit_waits(10)

    def launch(self):

        self.driver.launch_app(self.url)

        self.driver.max_window()

        self.driver.execute_script("1100")

        time.sleep(5)
        try:
            firstname = self.driver.find_element(Techlistlocators.first_name)
            firstname.send_keys("bobby")

            date1 = self.driver.find_element(Techlistlocators.lastname)
            date1.send_keys("korimella")

            gender = self.driver.find_element(Techlistlocators.gender)
            gender.click()

            experiance = self.driver.find_element(Techlistlocators.experiance)
            experiance.click()

            dateof = self.driver.find_element(Techlistlocators.dateofbirth)
            dateof.send_keys("01/10/199")

            profession = self.driver.find_element(Techlistlocators.profession)
            profession.click()

            tool = self.driver.find_element(Techlistlocators.tool)
            tool.click()

            country = Select(self.driver.find_element(Techlistlocators.country))
            country.select_by_visible_text("Asia")

            selenium_command = Select(self.driver.find_element(Techlistlocators.selenium_command))
            selenium_command.select_by_visible_text("Browser Commands")

            picture = self.driver.find_element(Techlistlocators.upload_photo)
            picture.send_keys("//home//bobby//Pictures//garuda_linux.png")

            button_click = self.driver.find_element(Techlistlocators.submit_button)
            button_click.click()
            return True
        except Exception as e:
            print("Error is",str(e))
            return False

        

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    s = APPTechList()
    s.launch()
    #s.close()
    #s.get_app_properties()

