import time

import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pageobjects.Login_Page import Login_Page_Class
from utlities.readconfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_1:
    driver = None
    login_url = ReadConfig.get_login_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    #log = loggerClass.getLogger()

    def test_orangehrm_title_01(self):
        if self.driver.title == "OrangeHRM":
           assert True
        else:
           assert False

    def test_OrangeHRM_Logo_02(self):
      time.sleep(2)
      self.lp = Login_Page_Class(self.driver)
      time.sleep(3)
      if self.lp.verify_logo():
          self.driver.save_screenshot(".\\screenshots\\test_OrangeHRM_Logo_pass.png")
          assert True
      else:
          self.driver.save_screenshot(".\\screenshots\\test_OrangeHRM_Logo_fail.png")
          assert False


    def test_Orangehrm_Login_03(self):
        time.sleep(2)
        self.lp = Login_Page_Class(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        time.sleep(2)
        if self.lp.verify_login() == "login pass":
            self.lp.click_menu_button()
            assert True
        else:
            assert False