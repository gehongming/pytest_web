#__author__="G"
#date: 2019/11/14

from selenium.webdriver.common.by import  By

class CgzxPageLocator:
    cancel_order=(By.XPATH,'//span[text()="取 消"]')

    yes=(By.XPATH,'//a[text()="取消订单"]')

    #导航栏
    dhl=(By.XPATH,'//i[@class="icon iconfont icon-fenzu colorGray1"]')
    #好货商品
    hhsp=(By.XPATH,'//span[@class="am-popover-item-content"]/div/i[@class="icon iconfont icon-daifahuo"]/parent::div')
    # wait_for_pay = (By.XPATH, '//li[text()="待付款"]')
    #
    # wait_for_pay_number=(By.XPATH,'//li[text()="待付款"]/span[@class="ml4 colorRed"]')

