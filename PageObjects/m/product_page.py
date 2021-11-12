from PageLocators.m.product_page_locator import ProductPageLocator as ppl
from .common import *


class ProductPage(BasePage):

    #隐形眼睛加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def yxyj(self):
        #选择花色及数量
        self.click(ppl.join_gwc,'点击加入购物车')
        self.click(ppl.yx_huase,'选择花色')
        self.click(ppl.yx_duoxuan,'进入多选模式')
        self.click(ppl.yx_dushu,'选择度数范围')
        self.click(ppl.yx_piliang,'进入批量设置')
        self.click(ppl.yx_shuliang,'选择数量')
        self.click(ppl.yx_queding,'确认选择数量')
        self.click(ppl.jiarujinhuodan,'加入购物车')


    # 护理液操作加入购物车
    @allure.step('选择护理液规格，加入购物车')
    def huliye(self,count):
        self.click(ppl.join_gwc, '点击加入购物车')
        self.input_text(ppl.hl_count,'选择数量',count)
        time.sleep(0.1)
        self.click_element(ppl.jiarujinhuodan, '加入购物车')


    # 定制片操作加入购物车
    @allure.step('选择定制片sku，加入购物车')
    def dingzhi(self,zyy,qj,zj,zw):
        self.click(ppl.join_gwc, '点击加入购物车')
        self.input_text(ppl.dz_zyy,'选择左右眼',zyy)
        self.input_text(ppl.dz_dzqj, '选择定制球镜', qj)
        self.input_text(ppl.dz_dzzj, '选择定制柱镜', zj)
        self.input_text(ppl.dz_zw, '选择轴位', zw)
        self.click(ppl.dz_count, '选择数量')
        self.click_element(ppl.dz_jiaruqingdan,'加入清单')
        time.sleep(1)
        self.click_element(ppl.jiarujinhuodan, '加入购物车')


# 多彩伴侣盒操作加入购物车
    @allure.step('选择伴侣盒sku，加入购物车')
    def banlvhe(self):
        self.click(ppl.join_gwc, '点击加入购物车')
        self.click(ppl.blh_count, '选择数量')
        time.sleep(2)
        self.click_element(ppl.jiarujinhuodan, '加入购物车')


# 镜片操作加入购物车
    @allure.step('选择镜片sku，加入购物车')
    def jingpian(self):
        self.click(ppl.join_gwc, '点击加入购物车')
        self.click(ppl.jp_count, '选择数量')
        time.sleep(2)
        self.click_element(ppl.jiarujinhuodan, '加入购物车')


    @allure.step('进入进货单')
    def go_jinhuodan(self):
        self.click(ppl.go_jinhuodan, '点击加入购物车')




