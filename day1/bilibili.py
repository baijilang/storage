import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions

driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/')
driver.maximize_window()

try:
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/input').send_keys('小熊flippy')
except selenium.common.exceptions as e:
    print('error',e)
finally:
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/form/div/button').click()
    
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul[1]/div/div[2]/div[1]/div/a').click()
handles = driver.window_handles
driver.switch_to.window(handles[2])
driver.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[1]').click()

time.sleep(10)
driver.quit()
