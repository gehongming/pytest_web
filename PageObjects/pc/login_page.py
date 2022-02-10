#__author__="G"
#date: 2019/6/15

from PageLocators.pc.login_page_locator import LoginPageLocator as loc
from .common import *


class LoginPage(BasePage):

    # 登录
    @allure.step('管理员登陆')
    def console_login(self, business_id, console_agent, passwd):
        time.sleep(0.1)
        self.click(loc.console, '选择管理端登陆')
        time.sleep(0.1)
        self.input_text(loc.business_id, '输入企业号', business_id)
        self.input_text(loc.console_account, '输入管理员账号', console_agent)
        self.input_text(loc.pwd, '输入密码', passwd)
        time.sleep(10)
        # self.input_text(loc.verify_code, '输入验证码', verify)
        self.click_element(loc.login,'登录')
        time.sleep(5)
        try:
            WebDriverWait(
                self.driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//span[text()="首页"]')))
            return True
        except BaseException:
            BasePage(self.driver).save_web_screenshot('登陆失败')
            return False

    # 登录
    @allure.step('座席登陆')
    def agent_code(self, business_id, agent_account, passwd):

        self.input_text(loc.business_id, '输入企业号', business_id)
        self.input_text(loc.agent_account, '输入座席账号',agent_account)
        self.input_text(loc.pwd, '输入密码', passwd)
        # self.input_text(loc.verify_code, '输入验证码', verify)
        self.click_element(loc.login,'登录')






