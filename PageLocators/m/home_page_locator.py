# __author__="G"
#date: 2019/6/15

from selenium.webdriver.common.by import By


class HomePageLocator:
    # 搜索框
    search_go = (By.XPATH, '//input[@placeholder="搜索 商品/品牌/类别"]')
    search = (By.ID, 'search')
    # 隐形商品链接    服务商品-彩片补货
    yx = (
        By.XPATH,
        '//li/a[@href="/product?productId=1544772850184507348"]/parent::li')
    # 护理用品链接   服务商品-护理液补货
    hl = (
        By.XPATH,
        '//li/a[@href="/product?productId=1544772850184507381"]/parent::li')
    # 定制片链接   服务商品-定制补货
    dz = (
        By.XPATH,
        '//li/a[@href="/product?productId=1544772850184507424"]/parent::li')
    # 多彩伴侣盒链接  服务商品-伴侣盒补货
    blh = (
        By.XPATH,
        '//li/a[@href="/product?productId=1544772850184507412"]/parent::li')
    # 镜片链接  服务商品-镜片补货
    jp = (
        By.XPATH,
        '//li/a[@href="/product?productId=1544772850184507393"]/parent::li')
