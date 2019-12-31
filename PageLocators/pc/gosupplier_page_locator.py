from selenium.webdriver.common.by import By
class GosupplierPageLocator:
    #仓库列表
    list_cangku=(By.XPATH,'//span[text()=" 仓库商品"]')
    #在售列表
    list_seller=(By.XPATH,'//span[text()=" 在售商品"]')

    #仓库/在售列表商品名称搜索框
    search_product_name=(By.XPATH,'//input[@ng-model="condition.productName"]')

    #仓库列表全选框  3
    all_check=(By.XPATH,'//div/div/div/span/input[@class="ng-pristine ng-untouched ng-valid ng-empty"]')

    # 在售列表全选框  3
    all_check_zaishou = (By.XPATH, '//div/div/span/input[@class="ng-pristine ng-untouched ng-valid ng-empty"]')

    #批量上架
    piliangshangjia=(By.XPATH,'//button[text()="批量上架"]')

    #批量下架
    piliangxijia=(By.XPATH,'//button[text()="批量下架"]')

    #返回首页
    back_home=(By.XPATH,'//a[text()="返回首页"]')

    #查询
    search=(By.XPATH,'//button[text()="查询"]')







