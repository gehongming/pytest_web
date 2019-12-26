#__author__="G"
#date: 2019/6/15

from selenium.webdriver.common.by import  By


class HomePageLocator:
    #搜索框
    search_go=(By.XPATH,'//input[@placeholder="搜索 商品/品牌/类别"]')
    search=(By.ID,'search')
    #隐形商品链接 海昌星眸日抛彩色隐形眼镜5片装
    yx=(By.XPATH,'//li/a[@href="/product?productId=6397722431108153347"]/parent::li')
    # 护理用品链接 卫康新视多功能隐形眼镜护理液355ml
    hl=(By.XPATH,'//li/a[@href="/product?productId=6398009929407397891"]/parent::li')
    #定制片链接   【定制片】酷视远视散光隐形眼镜定制片半年抛1片装
    dz = (By.XPATH,'//li/a[@href="/product?productId=1544772850182525335"]/parent::li')
    #多彩伴侣盒链接  3N还原仪清洗仓
    blh=(By.XPATH,'//li/a[@href="/product?productId=1544772850182546195"]/parent::li')
    # 镜片链接   凯米拓牌1.67折射率镜片防辐射
    jp = (By.XPATH,'//li/a[@href="/product?productId=1544772850182649314"]/parent::li')







