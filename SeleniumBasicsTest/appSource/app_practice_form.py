
from libCommon.selenium_helper import SeleniumHelper
import time
from selenium.webdriver.support.select import Select
from appSource.locators import LPraForm as l


class AppPracticeForm:

    def __init__(self):
        self.url = "https://www.techlistic.com/p/selenium-practice-form.html"
        self.helper = SeleniumHelper()
        self.driver = self.helper.initialize_driver()


    def launch(self):
        self.driver.get(self.url)
        return True

    def pra_form2(self):
        first_name = self.helper.element(l.first_name).send_keys("Atchyut")
        last_name = self.helper.element(l.last_name).send_keys("Ejjagiri")
        return True

    def close(self):
        self.helper.close()
        return True

if __name__ == "__main__":
    s = AppPracticeForm()
    s.launch()
    s.pra_form2()

    '''
    def practice_form1(self):
        first_name = self.helper.identify_element("name","firstname","Atchyut")
        last_name = self.helper.identify_element("name", "lastname", "Ejjagiri")
        gender = self.helper.click_element("id","sex-0")
        exp = self.helper.click_element("id","exp-3")
        date = self.helper.identify_element("id","datepicker","29 March 2021")
        pro = self.helper.click_element("xpath","//*[@id='post-body-3077692503353518311']/div/div/div[21]/label")
        tool1 = self.helper.click_element("id","tool-0")
        tool2 = self.helper.click_element("id","tool-2")
        continent = self.helper.select_values("id","continents","Europe")
        cmds = self.helper.driver.find_elements_by_xpath("selenium_commands")
        for cmd in cmds:
            if cmd == "Browser Commands":
                cmd.click()
                break
        photo = self.helper.identify_element("id","photo","C:\\Users\\91964\\Downloads\\atchyut photo.jpg")


        submit = self.helper.click_element("id","submit")
    """

    """
    def practice_form(self):
        try:
            self.helper.driver.implicitly_wait(5)
            first_name = self.helper.driver.find_element_by_name("firstname").send_keys("Atchyut")
            last_name = self.helper.driver.find_element_by_name("lastname").send_keys("Ejjagiri")
            gender = self.helper.driver.find_element_by_id("sex-0").click()
            exp = self.helper.driver.find_element_by_id("exp-3").click()
            date = self.helper.driver.find_element_by_id("datepicker").send_keys("23 March 2021")
            pro = self.helper.driver.find_element_by_xpath("//*[@id='post-body-3077692503353518311']/div/div/div[21]/label").click()
            tool1 = self.helper.driver.find_element_by_id("tool-0").click()
            tool2 = self.helper.driver.find_element_by_id("tool-2").click()
            continent = self.helper.driver.find_element_by_id("continents")
            drp = Select(continent)
            drp.select_by_visible_text("Asia")
            cmds = self.helper.driver.find_elements_by_xpath("selenium_commands")
            for cmd in cmds:
                if cmd == "Browser Commands":
                    cmd.click()
                    break
            submit = self.helper.driver.find_element_by_id("submit").click()
            time.sleep(5)
            self.helper.driver.close()
        except Exception as e:
            print(f"error = {e}")
            raise Exception("practice form not filled successfully")
        else:
            return True
    """

    def close(self):
        self.helper.close()
        return True

if __name__=="__main__":
    s = AppPracticeForm()
    s.launch()
    s.practice_form1()
    #c=s.close()
    '''

