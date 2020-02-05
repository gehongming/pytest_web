#__author__="G"
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
@pytest.fixture(scope="session",autouse=True)  #默认调用
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    #清除测试报告、截图目录
    # remove_files_in_dir(contants.reports_screen)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")

@pytest.fixture(scope="class")
def open_url_register_m():
    # 前置
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    driver.get(cd.registered_url_m)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def open_url_m():
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    driver.get(cd.base_url_m)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home(open_url_m):
    open_url_m.get('https://m.yjq.com')
    yield



@pytest.fixture(scope="class")
def open_url_register_pc():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.registered_url_pc)
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()

@pytest.fixture(scope="class")
def open_url_pc():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.base_url_pc)
    yield (driver)  # yield之前代码是前置，之后的代码就是后置。
    #h后置
    driver.quit()






