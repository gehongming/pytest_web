#__author__="G"
#date: 2019/10/31
from selenium.webdriver.common.by import  By


class ProductPageLocator:
    #隐形商品sku 花色 度数（批量设置）
    yx_huase=(By.XPATH,'//li[@class="swipe-item"][1]')
    yx_duoxuan = (By.XPATH, '//span[@class="more-choice-wrap"]')
    yx_dushu=(By.XPATH,'//div[text()="0-600度"]')
    yx_piliang=(By.XPATH,'//div[text()="批量设置"]')
    yx_shuliang=(By.XPATH,'//div[@class="sum-num"]/a[text()="+"]')
    yx_queding=(By.XPATH,'//button[text()="确定"]')



    #选择护理用品数量
    hl_count=(By.XPATH,'//a[text()="+"]')

    #定制片sku （左右眼 定制球镜  定制柱镜  轴位  数量 ）
    dz_zyy=(By.XPATH,'//input[@placeholder="请选择左右眼"]')
    dz_dzqj=(By.XPATH,'//input[@placeholder="请选择定制球镜"]')
    dz_dzzj = (By.XPATH, '//input[@placeholder="请选择定制柱镜"]')
    dz_zw = (By.XPATH, '//input[@placeholder="请选择轴位"]')
    dz_count = (By.XPATH, '//div[@class="custom-sum-box"]/a[text()="+"]')
    dz_jiaruqingdan=(By.XPATH,'//a[text()="加入清单"]')
    #加入清单成功提示
    dz_check_qingdan=(By.XPATH,'//span[text()="已加入已选清单!"]')

    #多彩伴侣盒sku
    blh_count = (By.XPATH, '//span[text()="纯洁白"]/parent::div/following-sibling::div[@class="action-wrap"]/a[text()="+"]')

    #镜片sku
    jp_count=(By.XPATH, '//span[text()="-3.00"]/parent::div/following-sibling::div[@class="list-value"]/span[text()="+0.00"]/parent::div/following-sibling::div[@class="action-wrap"]/a[text()="+"]')

##########################
    # 加入购物车（通用）----选择sku
    join_gwc=(By.XPATH,'//button[@class="add-car"]')
    #选择sku后，加入进货单(通用)
    jiarujinhuodan = (By.XPATH, '//a[text()="加入进货单"]')
    #进货单加入成功提示-隐形眼镜
    success_gwc=(By.XPATH,'//span[text()="加入进货单成功"]')
    # 进货单加入成功提示-护理液
    huliy_success_gwc=(By.XPATH,'//span[text()="加入购物车成功 您还可以继续添加商品规格"]')
    #导航栏
    dhl=(By.XPATH,'//img[@class="home"]')
    #好货商品
    haohuoshangpin=(By.XPATH,'//A[text()="好货商品"]')
    #进入进货单
    go_jinhuodan=(By.XPATH,'//div[@class="searchlast-buycar"]')
###########################