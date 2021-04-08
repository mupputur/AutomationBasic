from libCommon.selenium_helper import SeleniumHelper
import time

class AppMulWindows:

    def __init__(self):
        self.helper = SeleniumHelper()
        self.driver = self.helper.initialize_driver()
    def mul_windows(self):

        self.driver.get("http://www.google.co.in")
        self.driver.execute_script("window.open('https://www.gmail.com')")
        self.driver.switch_to_window(self.driver.window_handles[0])
        print(self.driver.title)


        self.driver.switch_to_window(self.driver.window_handles[1])
        print(self.driver.title)


        time.sleep(10)
if __name__ == "__main__":
    a10 = AppMulWindows()
    a10.mul_windows()