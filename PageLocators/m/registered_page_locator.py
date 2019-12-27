#__author__="G"
#date: 2019/11/13


from selenium.webdriver.common.by import By


class RegisteredPageLocator:
    #同意协议按钮
    check_agree=(By.XPATH,'//a[text()="确认"]')
    #注册手机号输入框
    phone=(By.XPATH,'//input[@placeholder="联系人手机号"]')
    #验证码输入框
    phone_code=(By.XPATH,'//input[@placeholder="4位数字"]')
    #获取验证码
    bindPhone__acceptCode=(By.XPATH,'//button[text()="获取验证码"]')
    #提交
    tijiao=(By.XPATH,'//a[@class="am-button am-button-primary"]')

    #店铺名称
    storename=(By.XPATH,'//input[@placeholder="虚拟店铺名称，不能重复"]')
    #所在地
    location=(By.XPATH,'//input[@placeholder="省市区"]')
    #省
    province=(By.XPATH,'//li[text()="新疆维吾尔自治区"]')
    #市
    city=(By.XPATH,'//li[text()="可克达拉市"]')
    #区
    area=(By.XPATH,'//li[text()="兵团六十七团"]')
    #详细地址
    address=(By.XPATH,'//input[@placeholder="请填写"]')
    #联系人
    contact=(By.XPATH,'//input[@placeholder="请填写真实姓名"]')
    #营业执照
    business_license=(By.XPATH,'//div[@class="am-wingblank am-wingblank-lg"]/div/div/div/div/div/div/input')
    #选择医疗许可证
    choose_medicallicense=(By.XPATH,'//input[@type="checkbox"]')
    #医疗许可证
    medical_license =(By.XPATH,'//div[@class="am-wingblank am-wingblank-lg"]/div/div/div/div/div/div/div/input')
    #下一步
    next=(By.XPATH,'//span[text()="下一步"]')





