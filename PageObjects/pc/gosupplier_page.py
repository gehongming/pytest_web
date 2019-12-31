import allure
from PageLocators.pc.gosupplier_page_locator import GosupplierPageLocator as gpl
from PageLocators.pc.home_page_locator import HomePageLocator as hpl
from common.basepage import BasePage
import time

class GosupplierPage(BasePage):


    #進入供貨中心
    @allure.step('进入供货中心')
    def go_ghzx(self):
        self.click_element(hpl.go_gosupplier_order,'进入供货中心')


    #上架
    @allure.step('进入供货中心-仓库列表，上架商品')
    def  shangjia(self,title):
        self.click_element(gpl.list_cangku,'进入仓库')
        self.input_text(gpl.search_product_name,'输入目标商品名称',title)
        self.click_element(gpl.search, '查询')
        time.sleep(1.5)
        self.click_element2(gpl.all_check,'点击全选')
        time.sleep(0.5)
        self.click_element(gpl.piliangshangjia,'批量上架')

    #回到首页
    @allure.step('回到首页')
    def  back_home(self):
        self.click_element(gpl.back_home,'回到首页')

    @allure.step('进入供货中心-在售列表，下架商品')
    def xiajia(self,title):
        self.click_element(gpl.list_seller,'进入在售列表')
        self.input_text(gpl.search_product_name,'输入目标商品名称',title)
        self.click_element(gpl.search,'查询')
        time.sleep(1.5)
        self.click_element2(gpl.all_check_zaishou,'点击全选')
        time.sleep(0.5)
        self.click_element(gpl.piliangxijia,'批量上架')
