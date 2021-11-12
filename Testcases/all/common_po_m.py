# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/12 15:29
@Auth ： ghm
@File ：base_po.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""


import time

import allure
import pytest
from urllib.parse import unquote

from common import contants
from common.file import get_filelist

from PageObjects.m.index_page import IndexPage as ip
from PageObjects.m.registered_page import RegisteredPage as rp

from PageObjects.m.cgzx_page import CgzxPage as cp
from PageObjects.m.home_page import HomePage as hp
from PageObjects.m.login_page import LoginPage as lp
from PageObjects.m.order_page import OrderPage as op
from PageObjects.m.product_page import ProductPage as pp
from PageObjects.m.shopping_page import ShopPage as sp
from PageObjects.pc.gosupplier_page import GosupplierPage as gp
from PageObjects.pc.login_page import LoginPage as lpc
from PageObjects.pc.index_page import IndexPage as ipc

from Testdates.m import registered_datas as rd
from Testdates.m import buy_datas as bd
from Testdates.pc import buy_datas as bdc




