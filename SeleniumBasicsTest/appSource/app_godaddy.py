from libCommon.selenium_helper import SeleniumHelper


class APPGoDaddy:

    def __init__(self):
        self.url = "https://www.godaddy.com/"
        self.helper = SeleniumHelper()

    def launch(self):
        self.helper.launch_app(self.url)
        return True

    def get_app_properties(self):
        return self.helper.get_title(),self.helper.get_cur_url()

    def maximize_app(self):
        self.helper.max_window()
        return True

    def get_source(self):
        return self.helper.get_page_source()

    def close(self):
        self.helper.close()
        return True

if __name__ == "__main__":
    s = APPGoDaddy()
    s.launch()
    #s.close()
    s.get_app_properties()

