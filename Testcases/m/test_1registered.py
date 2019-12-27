#__author__="G"
#date: 2019/6/15
#encoding:utf-8
import time

import allure
import pytest

from PageObjects.m.index_page import IndexPage as ip
from PageObjects.m.registered_page import RegisteredPage as rp
from Testdates.m import registered_datas as rd


@pytest.mark.usefixtures("open_url_register")
@allure.feature('微商城每日用例-注册')
class TestLogin:
#申请店铺不上传医疗许可证
    @pytest.mark.register2
    def test_login(self,open_url_register):
        time.sleep(0.1)
        rp(open_url_register).aggre()
        rp(open_url_register).check_phone(rd.zhanghao_data["phone"],rd.zhanghao_data["code"])
        time.sleep(1)
        assert True == ip(open_url_register).register_check()
        rp(open_url_register).register(rd.store_data["storename"],rd.store_data["address"],rd.store_data["contact"])
        rp(open_url_register).update_business(rd.store_data["b_address"])
        time.sleep(0.5)
        # rp(open_url_register).tijiao()
        # time.sleep(2)
        # assert  True==ip(open_url_register).success_register()

    # 申请店铺上传医疗许可证
    @pytest.mark.demo
    def test_login2(self,open_url_register):
        time.sleep(0.1)
        rp(open_url_register).aggre()
        rp(open_url_register).check_phone(rd.zhanghao_data["phone"],rd.zhanghao_data["code"])
        time.sleep(2)
        assert True == ip(open_url_register).register_check()
        rp(open_url_register).register(rd.store_data["storename"],rd.store_data["address"],rd.store_data["contact"])
        rp(open_url_register).update_business(rd.store_data["b_address"])
        rp(open_url_register).update_medical(rd.store_data["m_address"])
        rp(open_url_register).tijiao()
        time.sleep(0.8)
        assert True==ip(open_url_register).success_register()
        time.sleep(5)




















