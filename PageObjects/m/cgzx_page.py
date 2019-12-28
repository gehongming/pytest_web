#__author__="G"
#date: 2019/11/14

from selenium.webdriver.common.keys import Keys
import allure
from PageLocators.m.cgzx_page_locator import CgzxPageLocator as cpl
from common.basepage import BasePage
import  time

class CgzxPage(BasePage):
    @allure.step('从订单列表进入采购单')
    def go_jinhuodan(self):
        self.click(cpl.dhl, '点击单导航栏')
        time.sleep(0.5)
        self.click(cpl.jhd,'点击进货单')

    @allure.step('取消订单')
    def cancel_order_yes(self):
        self.click(cpl.dhl, '点击单导航栏')
        time.sleep(0.5)
        self.click(cpl.cgzx, '点击采购中心')
        time.sleep(0.5)
        a=int(self.get_element_text(cpl.num_state,'获取待付款数字'))
        self.click_element(cpl.cgzx_state,'进入待付款列表')
        time.sleep(2)
        for i in range (1,a+1):
            self.click_element2(cpl.button_quxiao,'取消订单')
            time.sleep(0.1)
            self.click_element2(cpl.again_quxiao,'确认')
            time.sleep(0.8)


    def cancel_order_no(self):
        pass