from libCommon.selenium_basic import SeleniumBasic


class SeleniumHelper(SeleniumBasic):

    def launch_app(self, url):
        self.driver.get(url)

    def close_app(self):
        self.close()

    def execute_script(self, param):
        self.driver.execute_script("window.scrollTo(0,"+ param +")")

    def find_element(self, param):
        return self.driver.find_element(*param)

    def click(self):
        self.click()

    def send_keys(self, text):
        self.send_keys(text)

    def select_by_visible_text(self,text):
        self.select_by_visible_text(text)


if __name__  == "__main__":
    # Module Test code goes here
    s = SeleniumHelper()
    s.launch_app("https://www.godaddy.com/")
    print(s.get_title())
    s.close_app()
