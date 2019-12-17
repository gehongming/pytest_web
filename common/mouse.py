#__author__="G"
#date: 2019/12/10

from selenium.webdriver.common.action_chains import ActionChains
from common import log
logger=log.get_logger(__name__)
import time
class Mouse:

    def __init__(self,driver):
        self.driver = driver



    #鼠标悬浮
    def move(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标悬浮在元素{}上'.format(ele))
        ac.move_to_element(self.driver.find_element(*ele)).perform()

    #鼠标点击
    def click(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标点击元素{}'.format(ele))
        try:
            ac.click(self.driver.find_element(*ele)).perform()
        except:
            # 日志
            logger.exception("鼠标点击元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    #鼠标右击
    def context_click(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标右击元素{}'.format(ele))
        ac.context_click(self.driver.find_element(*ele)).perform()

    #双击
    def  double_click(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标双击元素{}'.format(ele))
        ac.double_click(self.driver.find_element(*ele)).perform()

    #拖拽
    def  drag_and_drop(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标拖拽元素{}'.format(ele))
        ac.drag_and_drop(self.driver.find_element(*ele)).perform()

    #按住左键不松
    def click_and_hold(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标按住元素{}左键不松'.format(ele))
        ac.click_and_hold(self.driver.find_element(*ele)).perform()

    #释放
    def release(self,ele):
        ac = ActionChains(self.driver)
        logger.info('鼠标释放元素{}'.format(ele))
        ac.release(self.driver.find_element(*ele)).perform()

    def save_web_screenshot(self,img_doc):
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc,now)
        try:
            self.driver.save_screenshot(screenshot_dir +"/" + filepath)
            logger.info("网页截图成功。图片存储在：{}".format(screenshot_dir +"/" + filepath))
        except:
            logger.exception("网页截屏失败！")

