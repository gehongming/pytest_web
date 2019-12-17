
import time
import  allure
from PageLocators.m.product_page_locator import ProductPageLocator as ppl
from common.basepage import BasePage


class ProductPage(BasePage):

    #隐形眼睛加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def yxyj(self):
        #选择花色及数量
        self.tap(ppl.join_gwc,'点击加入购物车')
        self.tap(ppl.yx_huase,'选择花色')
        self.tap(ppl.yx_duoxuan,'进入多选模式')
        self.tap(ppl.yx_dushu,'选择度数范围')
        self.tap(ppl.yx_piliang,'进入批量设置')
        self.tap(ppl.yx_shuliang,'选择数量')
        self.tap(ppl.yx_queding,'确认选择数量')
        self.tap(ppl.join_gwc,'加入购物车')
    def yxyj_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

    # 护理液操作加入购物车
    @allure.step('选择护理液规格，加入购物车')
    def huliye(self,count):
        self.input_text(ppl.hl_count,'选择数量',count)
        self.click_element(ppl.join_gwc, '加入购物车')
    def hl_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

    # 定制片操作加入购物车
    @allure.step('选择定制片sku，加入购物车')
    def dingzhi(self,zyy,qj,zj,zw,c):
        self.input_text(ppl.dz_zyy,'选择左右眼',zyy)
        self.input_text(ppl.dz_dzqj, '选择定制球镜', qj)
        self.input_text(ppl.dz_dzzj, '选择定制柱镜', zj)
        self.input_text(ppl.dz_zw, '选择轴位', zw)
        self.input_text(ppl.dz_count, '选择数量', c)
        self.click_element(ppl.dz_jiaruqingdan,'加入清单')
        time.sleep(2)
        self.click_element(ppl.join_gwc, '加入购物车')
    def dz_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')
    def dz_success_qingdan(self):
        return self.get_element_text(ppl.dz_check_qingdan,'加入清单成功提示文案')

# 多彩伴侣盒操作加入购物车
    @allure.step('选择伴侣盒sku，加入购物车')
    def banlvhe(self,c):
        self.input_text(ppl.blh_count, '选择数量', c)
        time.sleep(2)
        self.click_element(ppl.join_gwc, '加入购物车')
    def blh_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

# 镜片操作加入购物车
    @allure.step('选择镜片sku，加入购物车')
    def jingpian(self,c):
        self.input_text(ppl.jp_count, '选择数量', c)
        time.sleep(2)
        self.click_element(ppl.join_gwc, '加入购物车')
    def jp_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')


