#__author__="G"
#date: 2019/11/14


from PageLocators.pc.cgzx_page_locator import CgzxPageLocator as cpl
from .common import *

class CgzxPage(BasePage):
    @allure.step('进入带付款列表，取消订单')
    def cancel_order_yes(self):
        self.click_element2(cpl.wait_for_pay,'进入待付款列表')
        a=int(self.get_element_text(cpl.wait_for_pay_number,'获取待付款数字'))

        for i in range (1,a+1):
            self.click_element(cpl.cancel_order,'取消订单')
            self.click_element(cpl.yes,'确认')
            time.sleep(0.8)


    def cancel_order_no(self):
        pass