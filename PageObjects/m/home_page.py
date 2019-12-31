#__author__="G"
#date: 2019/6/15

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import allure
from PageLocators.m.home_page_locator import HomePageLocator as hpl
from common.basepage import BasePage
import time

class HomePage(BasePage):

    #搜索商品
    @allure.step('搜索商品')
    def search(self,title):
        self.click(hpl.search_go,'去搜索页')
        self.input_text(hpl.search, '搜索商品', title,Keys.ENTER)

    #点击yx商品
    @allure.step('点击进入隐形眼镜商品详情页面')
    def click_yx(self):
        self.click_element(hpl.yx,'进入隐形商品详情页')

    #点击hl商品
    @allure.step('点击进入护理液商品详情页面')
    def click_hl(self):
        self.click_element(hpl.hl,'进入护理商品详情页面')

    # 点击dz商品
    @allure.step('点击进入定制商品详情页面')
    def click_dz(self):
        self.click_element(hpl.dz, '进入定制商品详情页面')

    #点击blh商品
    @allure.step('点击进入伴侣盒商品详情页面')
    def click_blh(self):
        self.click_element(hpl.blh,'进入伴侣盒商品详情页面并切换窗口')

    #点击jp商品
    @allure.step('点击进入镜片商品详情页面')
    def click_jp(self):
        self.click_element(hpl.jp,'进入镜片商品详情页面并切换窗口')







