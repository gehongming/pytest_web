# __author__="G"
#date: 2019/6/29
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/6/20

import pytest
from selenium import webdriver
from Testdates.all import common_datas as cd
from common import contants
from common.delete_history import *


# remove_files_in_dir(contants.reports_log)
# print('删除日志')
# remove_files_in_dir(contants.allure_results_dir)
# print('删除xml')


# session级别的
@pytest.fixture(scope="session", autouse=True)  # 默认调用
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    # 清除测试报告、截图目录
    # remove_files_in_dir(contants.reports_screen)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")


@pytest.fixture(scope="class")
def open_url():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver.get(cd.clink2_bj)
    yield (driver)  # yield之前代码是前置，之后的代码就是后置。
    # h后置
    # driver.quit()
