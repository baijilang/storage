from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.suning.com/')
driver.maximize_window()
driver.find_element(By.ID, 'searchKeywords').send_keys('私人飞机')
driver.find_element(By.ID, 'searchSubmit').click()

driver.find_element(By.XPATH, '//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_02:0070742680_11755985247"]').click()
# 进入其他窗口
handles = driver.window_handles
driver.switch_to.window(handles[1])

js = 'window.scrollTo(0,300)'
driver.execute_script(js)

driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[13]/a[3]").click()

driver.find_element(By.XPATH, '/html/body/div[38]/div/div[2]/div/div[1]/a').click()

time.sleep(5)
driver.quit()
