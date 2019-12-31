from selenium.webdriver.common.by import  By

class ShoppingPageLocator:
    #勾选店铺商品
    gogogo=(By.XPATH,'//span[text()="小明眼镜店cs002"]/ancestor::div[@class="am-list-line"]/preceding-sibling::div/label/span/input')
    #gogogo_2 =(By.XPATH,'//span[text()="丹阳市开发区镜色眼镜店"]/ancestor::div[@class="am-list-line"]/preceding-sibling::div/label/span/input')
    #去结算
    to_buyer=(By.XPATH,'//button[@class="btn-blue"]')
    #切换定制片
    check_dz=(By.XPATH,'//span[@class="am-badge" and text()="定制商品"]')
