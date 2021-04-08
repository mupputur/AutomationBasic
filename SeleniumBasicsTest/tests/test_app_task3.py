from appSource.app_user_regin_process import APPUserRegProcess
import unittest,logging,time

class TestUserRegProcessTask3(unittest.TestCase):

    def setUp(self) -> None:
        self.app=APPUserRegProcess()
        print(self._testMethodName)
        self.response = self.app.launch()

    def test1_0_lauch_app(self):
        self.assertTrue(self.response, "Failed to launch application")

    def test1_1_user_reg_pro(self):
        act_res = self.app.user_reg_pro()
        self.assertTrue(act_res, "Failed user registration process")

    def test1_2_var_user(self):
        act_res1 = self.app.val_user()
        self.assertTrue(act_res1, "Failed to invalid user")

    def test2_var_invalid_email(self):
        act_res2 = self.app.ver_invalid_email()
        self.assertTrue(act_res2, "Failed to valid email")

    def test3_var_manditory_error(self):
        act_res3 = self.app.ver_manditary_error()
        self.assertTrue(act_res3, "Failed to not manditory feilds error")

    def test4_incorrect_value_error(self):
        act_res4 = self.app.ver_incorrect_data()
        self.assertTrue(act_res4, "Failed to correct data")

if __name__=="__main__":
    unittest.main()

