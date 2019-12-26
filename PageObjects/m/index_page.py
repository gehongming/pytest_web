#__author__="G"
#date: 2019/6/15
import time
from common.basepage import BasePage
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageLocators.m.product_page_locator import ProductPageLocator as ppl


class IndexPage:
    def __init__(self,driver):
        self.driver=driver
    #登录成功校验
    def login_check(self):
        #判断结果获取失败截图
        try:
            self.driver.find_element_by_xpath('//a[text()="登录查看"]')
            BasePage(self.driver).save_web_screenshot('登陆失败')
            return False
        except:
            return True
    #加入购物车成功校验-加入购物车成功 您还可以继续添加商品规格
    def jiaru_success_2(self):
        try:

            self.driver.find_element(*ppl.huliy_success_gwc)
            return  True
        except:
            BasePage(self.driver).save_web_screenshot('加入购物车校验失败')
            return False

# 加入购物车成功校验-加入进货单成功
    def jiaru_success_1(self):
        try:
            self.driver.find_element(*ppl.success_gwc)
            return True
        except:
            BasePage(self.driver).save_web_screenshot('加入购物车校验失败')
            return False

            # 加入清单成功校验

    # 加入清单成功校验
    def jiaruqingdan_success(self):
        try:
            self.driver.find_element(*ppl.dz_check_qingdan)
            return True
        except:
            BasePage(self.driver).save_web_screenshot('加入清单校验失败')
            return False
    #进入店铺信息填写页校验
    def register_check(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,'//p[text() = "以下信息需要审核填写真实信息"]')))
            return  True
        except:
            BasePage(self.driver).save_web_screenshot('信息填写页面校验失败')
            return False
    #注册成功校验
    def success_register(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,'// p[text() = "提交成功"]')))
            return  True
        except:
            BasePage(self.driver).save_web_screenshot('注册校验失败')
            return False



