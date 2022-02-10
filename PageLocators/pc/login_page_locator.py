# __author__="G"
#date: 2019/11/14

from selenium.webdriver.common.by import By



class LoginPageLocator:

    console = (By.XPATH, '//li[text()=" 管理员登录 "]')  # 管理员登陆
    business_id = (By.XPATH, '//input[@placeholder="企业编号"]')  # 企业编号
    console_account = (By.XPATH, '//input[@placeholder="管理员账号"]')  # 管理员账号
    agent_account = (By.XPATH, '//input[@placeholder="座席号"]')  # 座席账号
    pwd = (By.XPATH, '//input[@placeholder="密码"]')  # 管理员密码
    verify_code = (By.XPATH, '//input[@placeholder="验证码"]')  # 验证码

    login = (By.XPATH, '//button[text()=" 登录系统 "]')

