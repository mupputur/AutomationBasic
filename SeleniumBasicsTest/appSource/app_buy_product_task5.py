from libCommon.selenium_helper import SeleniumHelper
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class AppBuyProduct:

    def __init__(self):
        self.helper = SeleniumHelper()
        self.driver = self.helper.initialize_driver()

    def lauch_app(self):
        try:
            url = "http://automationpractice.com/index.php"
            self.helper.launch_app(url)
            return True
        except:
            raise Exception("failed launch application")
        #else:
            #return True
    """
    def login_app1(self):
        login = self.helper.click_element("class_name","login")
        email = self.helper.identify_element("id","email","eak403@gmail.com")
        passwd = self.helper.identify_element("id","passwd","Samata@47")
        sign_in = self.helper.click_element("id","SubmitLogin")"""

    def login_app(self):
        try:
            login = self.driver.find_element_by_class_name("login").click()
            email = self.driver.find_element_by_id("email").send_keys("eak403@gmail.com")
            passwd = self.driver.find_element_by_id("passwd").send_keys("Samata@47")
            sign_in = self.driver.find_element_by_id("SubmitLogin").click()
        except:
            raise Exception("Failed to login application")
        else:
            return True

    def move_product(self):
        try:
            women = self.driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a")
            t_shirt = self.driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/ul/li[1]/ul/li[1]/a")
            actions = ActionChains(self.driver)
            actions.move_to_element(women).move_to_element(t_shirt).click().perform()
        except:
            raise Exception("failed to  select the product")
        else:
            return True

    def click_more_button(self):
        try:
            self.driver.implicitly_wait(30)
            wait = WebDriverWait(self.driver, 30)
            more = wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='center_column']/ul/li/div/div[2]/div[2]/a[2]/span")))
            more.click()
        except:
            raise Exception("failed to click more button")
        else:
            return True

    def product_add_to_cart(self):
        try:
            quantity = self.driver.find_element_by_xpath("//*[@id='quantity_wanted_p']/a[2]/span/i").click()
            drp_large = self.helper.select_values("id", "group_1", "L")
            color = self.driver.find_element_by_xpath("//*[@id='color_14']").click()
            add_cart = self.driver.find_element_by_xpath("//*[@id='add_to_cart']/button/span").click()
        except:
            raise Exception("failed to add products to cart")
        else:
            return True

    def buy_products(self):
        try:
            check_out = self.driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a").click()
            check_out1 = self.driver.find_element_by_xpath("//*[@id='center_column']/p[2]/a[1]").click()
            address = self.driver.find_element_by_name("processAddress").click()
            agree = self.driver.find_element_by_id("cgv").click()
            order = self.driver.find_element_by_name("processCarrier").click()
            cart = self.driver.find_element_by_xpath("//*[@id='header']/div[3]/div/div/div[3]/div/a").text
            print(cart)
        except:
            raise Exception("failed to buy products")
        else:
            return True

    def wishlist(self):
        try:
            wishlist = self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li/div/div/div[3]/div/div[3]/div[1]/a").click()
            error = self.driver.find_element_by_xpath("//*[@id='category']/div[2]/div/div/div/div/p").text
            print(error)
        except:
            raise Exception("failed to wishlist")
        else:
            return True

    def var_total_price(self):
        try:
            drp_large = self.helper.select_values("id", "group_1", "M")
            color = self.driver.find_element_by_xpath("//*[@id='color_14']").click()
            add_cart = self.driver.find_element_by_xpath("//*[@id='add_to_cart']/button/span").click()
            check_out = self.driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a").click()
            self.driver.implicitly_wait(20)
            plus_clk = self.driver.find_element_by_class_name("icon-plus").click()

            wait = WebDriverWait(self.driver, 30)
            #quantity = wait.until(ec.presence_of_element_located((By.NAME, "quantity_1_1_0_0"))).text
            #print(quantity)
            self.driver.implicitly_wait(30)
            price = wait.until(ec.visibility_of_element_located((By.ID, "total_product_price_1_4_470268"))).text
            print(price)

        except:
            raise Exception("failed to verify total price")
        else:
            return True

    def close_app(self):
        self.helper.close()





    """
    def buy_product(self):
        try:
            women = self.driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a")
            t_shirt = self.driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/ul/li[1]/ul/li[1]/a")
            actions = ActionChains(self.driver)
            actions.move_to_element(women).move_to_element(t_shirt).click().perform()
            self.driver.implicitly_wait(20)
            wait = WebDriverWait(self.driver,30)
            more =wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='center_column']/ul/li/div/div[2]/div[2]/a[2]/span")))
            more.click()
            #more = self.driver.find_element_by_xpath("//*[@id='center_column']/ul/li/div/div/div[3]/div/div[2]/a[2]/span").click()
            quantity = self.driver.find_element_by_xpath("//*[@id='quantity_wanted_p']/a[2]/span/i").click()
            drp_large = self.helper.select_values("id","group_1","L")
            color = self.driver.find_element_by_xpath("//*[@id='color_14']").click()
            add_cart = self.driver.find_element_by_xpath("//*[@id='add_to_cart']/button/span").click()
            check_out = self.driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a").click()
            check_out1 = self.driver.find_element_by_xpath("//*[@id='center_column']/p[2]/a[1]").click()
            address = self.driver.find_element_by_name("processAddress").click()
            agree = self.driver.find_element_by_id("cgv").click()
            order = self.driver.find_element_by_name("processCarrier").click()
            cart = self.driver.find_element_by_xpath("//*[@id='header']/div[3]/div/div/div[3]/div/a").text
            print(cart)
        except:
            raise Exception("failed buy product process")
        else:
            return True
    """
if __name__ == "__main__":
    a5 = AppBuyProduct()
    a5.lauch_app()
    a5.login_app()
    a5.move_product()
    a5.click_more_button()
