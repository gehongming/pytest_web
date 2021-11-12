#__author__="G"
#date: 2019/6/15

from PageLocators.pc.login_page_locator import LoginPageLocator as loc
from .common import *


class LoginPage(BasePage):

    #登录
    @allure.step('验证码登录')
    def login_code(self,user,passwd):
        #切换置快捷登录输入账号密码
        self.click_element(loc.kuajie_login,'选择快捷登录')
        self.input_text(loc.uesr_loc,'输入手机号',user)
        # self.input_text(loc.password, '输入验证码',passwd,Keys.ENTER)
        self.input_text(loc.password, '输入验证码', passwd)
        self.click_element(loc.login,'登录')







