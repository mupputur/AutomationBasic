
import unittest,sys,HtmlTestRunner
sys.path.append("C:\\Users\91964\PycharmProjects\SeleniumBasicsTest")
from appSource.app_buy_product_task5 import AppBuyProduct
test_results_path= "C:\\Users\\91964\\PycharmProjects\\SeleniumBasicsTest\\Reports"


class TestAppBuyProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.app = AppBuyProduct()
        print(self._testMethodName)
        self.response = self.app.lauch_app()

    def test_1_buy_product(self):
        self.assertTrue(self.response, "failed to lauch application")
        res_login = self.app.login_app()
        self.assertTrue(res_login,"failed to login application")
        res_move = self.app.move_product()
        self.assertTrue(res_move, "failed to move to product")
        res_more = self.app.click_more_button()
        self.assertTrue(res_more, "failed to click more button")
        res_cart = self.app.product_add_to_cart()
        self.assertTrue(res_cart, "failed to product add to cart")
        res_buy_pro = self.app.buy_products()
        self.assertTrue(res_buy_pro, "failed to buy product")

    def test_2_wishlist(self):
        self.assertTrue(self.response, "failed to lauch application")
        res_move = self.app.move_product()
        self.assertTrue(res_move, "failed to move to product")
        res_wishlist = self.app.wishlist()
        self.assertTrue(res_wishlist, "failed to wishlist")

    def test_3_total_price(self):
        self.assertTrue(self.response, "failed to lauch application")
        res_login = self.app.login_app()
        self.assertTrue(res_login, "failed to login application")
        res_move = self.app.move_product()
        self.assertTrue(res_move, "failed to move to product")
        res_more = self.app.click_more_button()
        self.assertTrue(res_more, "failed to click more button")
        res_cart = self.app.product_add_to_cart()
        self.assertTrue(res_cart, "failed to product add to cart")
        res_price = self.app.var_total_price()
        self.assertTrue(res_price, "failed to varify the total price")

    def tearDown(self) -> None:
        self.app.close_app()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = test_results_path))


