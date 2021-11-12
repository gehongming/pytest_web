# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/12 15:29
@Auth ： ghm
@File ：base_po.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""


import time
from urllib.parse import unquote
import allure
import pytest

from common import contants
from common.file import get_filelist


from PageObjects.pc.cgzx_page import CgzxPage as cp
from PageObjects.pc.home_page import HomePage as hp
from PageObjects.pc.index_page import IndexPage as ip
from PageObjects.pc.login_page import LoginPage as lp
from PageObjects.pc.order_page import OrderPage as op
from PageObjects.pc.product_page import ProductPage as pp
from PageObjects.pc.shopping_page import ShopPage as sp
from PageObjects.pc.gosupplier_page import GosupplierPage as gp
from PageObjects.pc.registered_page import RegisteredPage as rp


from Testdates.pc import buy_datas as bdc
from Testdates.pc import registered_datas as rd
from Testdates.pc import buy_datas as bd




