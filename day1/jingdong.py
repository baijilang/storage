import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # 创建浏览器，打开网址，最大化窗口
    driver = webdriver.Chrome()
    driver.get('https://www.jd.com')
    driver.maximize_window()

    # 定位搜索输入框并查找
    driver.find_element(By.ID, 'key').send_keys('外星人笔记本')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button').click()
    time.sleep(3)

    # 滚动
    # js = 'window.scrollTo(0,300)'
    # driver.execute_script(js)

    # 定位并点击进入一项
    driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[5]/div/div[1]/a/img').click()

    # 将窗口转到某一元素所在的位置 element = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div/div[
    # 2]/ul/li[5]/div/div[1]/a/img').click() driver.execute_script('arguments[0].scrollIntoView()',
    # element) 获取所有的窗口的句柄 handles = driver.get_window_rect()  # 窗口的大小，位置

    # 列表当前所有窗口，并转换所在窗口
    handles = driver.window_handles
    print(handles)
    driver.switch_to.window(handles[1])

    # 展示当前窗口的标题，验证是否成功更换窗口
    # title = driver.title
    # print(title)

    driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div[5]/div[22]/a[2]').click()
except Exception as e:
    print('error:', e)
except selenium.common.exceptions.NoSuchElementException as e:
    print('error:', e)
finally:
    global driver
    time.sleep(5)
    driver.quit()
