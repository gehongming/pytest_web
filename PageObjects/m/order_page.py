# __author__="G"
# date: 2019/6/15

from PageLocators.m.order_page_locator import OrderPageLocator as op
from .common import *


class OrderPage(BasePage):
    # 留言生成订单
    @allure.step('生成订单')
    def generate_orders(self, messaage):
        self.input_text(op.gogogo, '输入留言', messaage)
        time.sleep(0.3)
        self.click_element(op.to_buyer, '生成订单')
