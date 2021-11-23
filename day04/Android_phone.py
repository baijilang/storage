import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import By
from selenium.common import exceptions as exp


class Android_app:

    def __init__(self, driver=webdriver.Remote):
        if not isinstance(driver, webdriver.Remote):
            # 运行器在测试类中已连接
            url = '127.0.0.1:4723/wd/hub'
            param = {
                'deviceName': '127.0.0.1:62001',
                'platformName': 'Android',
                'platformVersion': '5.1.1',
                'appPackage': 'com.sina.weibo',
                'appActivity': 'com.sina.weibo.SplashActivity'}
            self.driver = webdriver.Remote(url, param)
        else:
            self.driver = driver

    def agree(self):
        TouchAction(self.driver).tap(x=468, y=798).perform()

    def log_page(self, account, password):
        try:
            # 进入登录界面
            self.agree()
            ele1 = self.driver.find_element_by_accessibility_id("我")
            ele1.click()
            time.sleep(2)
            # 切换到账号密码登录模式
            self.driver.find_element_by_id("com.sina.weibo:id/iv_psw").click()
            # 账号和密码
            ele2_1 = self.driver.find_element_by_id('com.sina.weibo:id/et_login_view_uname')
            ele2_1.send_keys(account)
            ele2_2 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw")
            ele2_2.send_keys(password)
            # 协议
            ele2_3 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_protocol")
            ele2_3.click()
            time.sleep(2)
            # 获取登录结果信息
        except exp.InvalidSwitchToTargetException as e:
            print('login_page error:', e)
        except exp.NoSuchElementException as e:
            print('login_page error:', e)
        finally:
            info = ''
            try:
                info = self.driver.find_element_by_id("com.sina.weibo:id/titleLeft")
            except exp:
                print('Login defeated')
            else:
                info = self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_tips")
            self.close_driver()
            return info

    def close_driver(self):
        try:
            self.driver.quit()
        except exp:
            print(' Quit')

    def video_page(self):
        try:
            self.agree()
            ele4 = self.driver.find_element_by_accessibility_id("视频")
            ele4.click()
            time.sleep(2)
            TouchAction(self.driver).press(x=308, y=796).move_to(x=297, y=291).release().perform()
            TouchAction(self.driver).press(x=353, y=902).move_to(x=395, y=392).release().perform()

            time.sleep(10)
        except exp.InvalidSwitchToTargetException as e:
            print('video_page error:', e)
        except exp.NoSuchElementException as e:
            print('login_page error:', e)
        finally:
            self.driver.quit()

    def find_page(self, key):
        try:
            self.agree()
            ele5 = self.driver.find_element_by_accessibility_id("发现")
            ele5.click()
            ele6 = self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/"
                                                      "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                      "android.widget.TabHost/android.widget.FrameLayout[2]/"
                                                      "android.widget.FrameLayout/android.widget.LinearLayout/"
                                                      "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                                      "android.widget.RelativeLayout/android.widget.RelativeLayout/"
                                                      "android.widget.FrameLayout/android.widget.FrameLayout[2]/"
                                                      "android.widget.ViewFlipper/android.widget.RelativeLayout/"
                                                      "android.widget.RelativeLayout/android.widget.LinearLayout/"
                                                      "android.widget.EditText")
            ele6.click()
            ele7 = self.driver.find_element(By.ID, "com.sina.weibo:id/tv_search_keyword")
            ele7.send_keys(key)
            ele8 = self.driver.find_element_by_accessibility_id("搜索图标")
            ele8.click()
            TouchAction(self.driver).tap(x=249, y=146).perform()
            TouchAction(self.driver).tap(x=249, y=146).perform()
            TouchAction(self.driver).tap(x=59, y=412).perform()
            TouchAction(self.driver).tap(x=None, y=None).perform()
            ele9 = self.driver.find_element(By.ID, "com.sina.weibo:id/detail_activity_header_left_button_text")
            ele9.click()
            ele10 = self.driver.find_element(By.ID, "com.sina.weibo:id/back")
            ele10.click()
            ele11 = self.driver.find_element(By.ID, "com.sina.weibo:id/btn_search_or_back")
            ele11.click()
        except exp.InvalidSwitchToTargetException as e:
            print('video_page error:', e)
        except exp.NoSuchElementException as e:
            print('login_page error:', e)
        finally:
            self.driver.quit()

    def message_page(self):
        try:
            self.agree()
            ele12 = self.driver.find_element_by_accessibility_id("消息")
            ele12.click()
            ele13 = self.driver.find_element(By.ID, "com.sina.weibo:id/et_login_view_phone")
            ele13.click()
            ele13.send_keys("01234567890")
            ele14 = self.driver.find_element(By.ID, "com.sina.weibo:id/tv_login_view_resent")
            ele14.click()
            ele15 = self.driver.find_element(By.ID, "com.sina.weibo:id/iv_title_back")
            ele15.click()
        except exp.InvalidSwitchToTargetException as e:
            print('video_page error:', e)
        except exp.NoSuchElementException as e:
            print('login_page error:', e)
        finally:
            self.driver.quit()
