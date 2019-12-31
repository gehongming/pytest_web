#__author__="G"
#date: 2019/6/15
#encoding:utf-8
import time
from urllib.parse import unquote

import allure
import pytest

from PageObjects.m.cgzx_page import CgzxPage as cp
from PageObjects.m.home_page import HomePage as hp
from PageObjects.m.index_page import IndexPage as ip
from PageObjects.m.login_page import LoginPage as lp
from PageObjects.m.order_page import OrderPage as op
from PageObjects.m.product_page import ProductPage as pp
from PageObjects.m.shopping_page import ShopPage as sp
from Testdates.m import buy_datas as bd
from common import contants
from common.file import get_filelist
@allure.feature("微商城每日用例-加购")
@pytest.mark.usefixtures("open_url1")
class TestLogin:

#密码登录
    @pytest.mark.demo
    @allure.story('登录')
    @allure.title('测试登录正常')
    @allure.description('这是微商城密码登录的成功用例')
    def test_login(self,open_url1):
        try:
            lp(open_url1).login_pwd(bd.login_data["user"],bd.login_data["passwd"])
            time.sleep(1)
            assert True == ip(open_url1).login_check()
            assert unquote(open_url1.current_url, encoding='utf-8') == 'https://m.yjq.com/'
        except AssertionError as e:
            Filelist = get_filelist(contants.reports_screen)
            with open(Filelist[0], "rb") as f:
                context = f.read()
                allure.attach(context, "错误图片", attachment_type=allure.attachment_type.PNG)
                raise e


#隐形眼镜加入购物车

    @pytest.mark.demo
    @allure.story('微商城隐形眼镜加入购物车')
    @allure.title('微商城隐形眼镜加入购物车')
    @allure.description('这是隐形眼镜加入购物车的成功用例')
    def test_buy_yx(self,open_url1):
        open_url1.get('https://m.yjq.com/search-page')
        #搜索隐形眼镜商品
        hp(open_url1).search(bd.success_data_yxyj["title"])
        time.sleep(1)
        assert unquote(open_url1.current_url, encoding='utf-8')== bd.success_data_yxyj["check_url"]
        #点击进入商品详情页
        hp(open_url1).click_yx()
        #验证是否进入
        time.sleep(1)
        assert unquote(open_url1.current_url, encoding='utf-8')==bd.success_data_yxyj["check_product_url"]
        #选择sku
        pp(open_url1).yxyj()
        time.sleep(0.5)
        assert True == ip(open_url1).jiaru_success_1()

#护理液加入购物车
    @pytest.mark.usefixtures("home")
    @pytest.mark.demo
    @allure.story('微商城护理液加入购物车')
    @allure.title('微商城护理液加入购物车')
    @allure.description('这是护理液加入购物车的成功用例')
    def test_buy_hl(self, open_url1):
        hp(open_url1).search(bd.success_data_huliye["title"])
        time.sleep(2)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_huliye["check_url"]
        # 点击进入商品详情页
        hp(open_url1).click_hl()
        # 验证是否进入
        time.sleep(1)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_huliye["check_product_url"]
        # 选择数量并加入购物车
        pp(open_url1).huliye('1')
        time.sleep(0.5)
        assert True == ip(open_url1).jiaru_success_2()

#定制片加入购物车
    @pytest.mark.usefixtures("home")
    @pytest.mark.demo
    @allure.story('微商城定制片加入购物车')
    @allure.title('微商城定制片加入购物车')
    @allure.description('这是定制片加入购物车的成功用例')
    def test_buy_dzp(self, open_url1):
        hp(open_url1).search(bd.success_data_dzp["title"])
        time.sleep(1)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_dzp["check_url"]
        # 点击进入商品详情页
        hp(open_url1).click_dz()
        # 验证是否进入
        time.sleep(1)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_dzp["check_product_url"]
        # 选择sku并加入购物车
        pp(open_url1).dingzhi(bd.success_data_dzp["sku"][0],bd.success_data_dzp["sku"][1],bd.success_data_dzp["sku"][2],
        bd.success_data_dzp["sku"][3])
        time.sleep(1)
        assert True == ip(open_url1).jiaru_success_1()

#多彩伴侣盒加入购物车
    @pytest.mark.usefixtures("home")
    @pytest.mark.demo
    @allure.story('微商城伴侣盒加入购物车')
    @allure.title('微商城伴侣盒加入购物车')
    @allure.description('这是伴侣盒加入购物车的成功用例')
    def test_buy_blh(self, open_url1):
        hp(open_url1).search(bd.success_data_blh["title"])
        time.sleep(1)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_blh["check_url"]
        # 点击进入商品详情页,并切换窗口
        hp(open_url1).click_blh()
        # 验证是否进入
        time.sleep(1)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_blh["check_product_url"]
        # 选择sku并加入购物车
        pp(open_url1).banlvhe()
        time.sleep(1)
        assert True == ip(open_url1).jiaru_success_1()

#镜片加入购物车
    @pytest.mark.usefixtures("home")
    @pytest.mark.demo
    @allure.story('微商城镜片加入购物车')
    @allure.title('微商城镜片加入购物车')
    @allure.description('这是镜片加入购物车的成功用例')
    def test_buy_jp(self, open_url1):
        hp(open_url1).search(bd.success_data_jp["title"])
        time.sleep(2)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_jp["check_url"]
        # 点击进入商品详情页,并切换窗口
        hp(open_url1).click_jp()
        # 验证是否进入
        time.sleep(1)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_jp["check_product_url"]
        # 选择sku并加入购物车
        pp(open_url1).jingpian()
        time.sleep(1)
        assert True == ip(open_url1).jiaru_success_1()

#进入购物车,选择普通商品并结算
    @pytest.mark.demo
    @allure.story('微商城购物车结算')
    @allure.title('微商城购物车结算')
    @allure.description('这是普通片下单的成功用例')
    def test_orders(self,open_url1):
        pp(open_url1).go_jinhuodan()
        time.sleep(1.5)
        sp(open_url1).check_goods()
        time.sleep(2)
        op(open_url1).generate_orders(bd.to_order["message"])
        time.sleep(3)
        assert open_url1.current_url==bd.to_order["check_url"]

#进入购物车,选择定制商品并结算
    @pytest.mark.demo
    @allure.story('微商城购物车结算')
    @allure.title('微商城购物车结算')
    @allure.description('这是定制片下单的成功用例')
    def test_dz_orders(self,open_url1):
        cp(open_url1).go_jinhuodan()
        time.sleep(0.8)
        sp(open_url1).check_goods_dz()
        time.sleep(0.3)
        op(open_url1).generate_orders(bd.to_order["message"])
        time.sleep(3)
        assert open_url1.current_url==bd.to_order["check_url"]

#取消订单
    @pytest.mark.demo
    @allure.story('微商城取消订单')
    @allure.title('微商城取消订单')
    @allure.description('这是取消采购中心订单的成功用例')
    def test_cancel_order_yes(self,open_url1):
        time.sleep(0.2)
        cp(open_url1).cancel_order_yes()
        time.sleep(3)





















