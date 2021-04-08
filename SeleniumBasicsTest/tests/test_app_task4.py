from appSource.app_ec_amazon_ass1 import APPEcAmazonAss1
import unittest


class TestEcAmazonTask4(unittest.TestCase):

    def setUp(self) -> None:
        self.app=APPEcAmazon()
        print(self._testMethodName)
        self.response = self.app.launch()

    def test1_0_Launch_browser(self):
        self.assertTrue(self.response, "Failed to launch application")

    def test1_1_user_reg(self):
       act_res = self.app.user_reg()
       self.assertTrue(act_res, "Failed user registration process")


    def test1_2_var_invalid_mobile_num(self):
        act_res1 =self.app.var_invalid_mobile_number()
        self.assertTrue(act_res1, "Failed to valid mobile number")

    def test1_3_var_name(self):
        exp_name ="Enter your name"
        act_name =self.app.var_textboxs()[0]
        print(f"actname={act_name} expname={exp_name}")
        self.assertEqual(act_name,exp_name,"Failed to varify name")

    def test1_4_var_pass(self):
        exp_pass ="Enter your password"
        act_pass = self.app.var_textboxs()[1]
        print(f"actpass={act_pass} exppass={exp_pass}")
        self.assertEqual(act_pass, exp_pass, "Failed to varify password")

    def tearDown(self) -> None:
        self.app.close()

if __name__ == "__main__":
    unittest.main()