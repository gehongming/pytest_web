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

from PageObjects.pc.login_page import LoginPage as lp

from Testdates.all import common_datas as cd





