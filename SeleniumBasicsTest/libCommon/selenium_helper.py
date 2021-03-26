from libCommon.selenium_basic import SeleniumBasic


class SeleniumHelper(SeleniumBasic):

    def launch_app(self, url):
        self.driver.get(url)

    def close_app(self):
        self.close()

if __name__  == "__main__":
    # Module Test code goes here
    s = SeleniumHelper()
    s.launch_app("https://www.godaddy.com/")
    print(s.get_title())
    s.close_app()
