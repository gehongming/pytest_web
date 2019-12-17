#__author__="G"
#date: 2019/6/15
from selenium.webdriver.common.keys import Keys
import allure
from PageLocators.m.login_page_locator import LoginPageLocator as loc
from common.basepage import BasePage
import  time
from common.mouse import Mouse

class LoginPage(BasePage):

    #登录
    @allure.step('验证码登录')
    def login_pwd(self,user,passwd):
        #输入账号密码
        self.input_text(loc.uesr_loc,'输入手机号',user)
        self.input_text(loc.password, '输入密码', passwd)
        #点击无效使用回车代替
        self.input_text(loc.login,'触发登录',Keys.ENTER)










