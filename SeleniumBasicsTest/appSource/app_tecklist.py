from libCommon.selenium_helper import SeleniumHelper
import time
from sourcelocators.techlocators import Techlistlocators

class APPTechList:

    def __init__(self):
        self.url = "https://www.techlistic.com/p/selenium-practice-form.html"
        self.ally = SeleniumHelper()
        self.ally.implecit_waits(10)

    def fill_form(self):

        self.ally.launch_app(self.url)

        self.ally.max_window()

        self.ally.execute_script("1100")

        time.sleep(5)

        try:
            firstname = self.ally.find_element(Techlistlocators.first_name)
            firstname.send_keys("bobby")

            date1 = self.ally.find_element(Techlistlocators.lastname)
            date1.send_keys("korimella")

            gender = self.ally.find_element(Techlistlocators.gender)
            gender.click()

            experiance = self.ally.find_element(Techlistlocators.experiance)
            experiance.click()

            dateof = self.ally.find_element(Techlistlocators.dateofbirth)
            dateof.send_keys("01/10/199")

            profession = self.ally.find_element(Techlistlocators.profession)
            profession.click()

            tool = self.ally.find_element(Techlistlocators.tool)
            tool.click()

            country = self.ally.Select(self.ally.find_element(Techlistlocators.country))
            country.select_by_visible_text("Asia")

            selenium_command = self.ally.Select(self.ally.find_element(Techlistlocators.selenium_command))
            selenium_command.select_by_visible_text("Browser Commands")

            picture = self.ally.find_element(Techlistlocators.upload_photo)
            picture.send_keys("//home//bobby//Pictures//garuda_linux.png")

            button = self.ally.find_element(Techlistlocators.submit_button)
            button.click()
            return True
        except Exception as e:
            print("Error is",str(e))
            return False

        

    def close(self):
        self.ally.close()


if __name__ == "__main__":
    s = APPTechList()
    s.fill_form()
    #s.close()
    #s.get_app_properties()

