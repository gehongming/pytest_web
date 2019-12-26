#__author__="G"
#date: 2019/11/14

from selenium.webdriver.common.by import  By

class CgzxPageLocator:


    #导航栏
    dhl=(By.XPATH,'//i[@class="icon iconfont icon-fenzu colorGray1"]')
    #好货商品
    hhsp=(By.XPATH,'//span[@class="am-popover-item-content"]/div/i[@class="icon iconfont icon-daifahuo"]/parent::div')
    #进货单
    jhd=(By.XPATH,'//span[@class="am-popover-item-content"]/div/i[@class="icon iconfont icon-jinhuodan"]/parent::div')
    #采购中心
    cgzx=(By.XPATH,'//span[@class="am-popover-item-content"]/div/i[@class="icon iconfont icon-gerenzhongxin"]/parent::div')


    #采购中心待付款数量
    num_state=(By.XPATH,'//div[text()="待付款"]/following-sibling::span[@class="counttips"]')
    #采购中心待付款列表入口
    cgzx_state=(By.XPATH,'//div[text()="待付款"]/parent::div')

    #待付款取消按钮
    button_quxiao=(By.XPATH,'//div[@aria-hidden="false"]/div/div/div/div//span[text()="取 消"]')
    #确认取消
    again_quxiao=(By.XPATH,'//a[text()="取消订单"]')


    # wait_for_pay = (By.XPATH, '//li[text()="待付款"]')
    #
    # wait_for_pay_number=(By.XPATH,'//li[text()="待付款"]/span[@class="ml4 colorRed"]')

