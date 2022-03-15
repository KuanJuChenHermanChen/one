#!/usr/bin/env python
# coding: utf-8

# In[50]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 使用 Chrome 的 WebDriver
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service = service)

# 開啟網頁
driver.get("https://plvr.land.moi.gov.tw/DownloadOpenData")

sleep(1)

#點選跳到「非本期下載」
driver.find_element(by = By.XPATH, value='//*[@id="ui-id-2"]').click()

sleep(1)

#選擇108年第二季
Select(driver.find_element(By.ID,'historySeason_id')).select_by_value('108S2')

#選擇CSV檔
Select(driver.find_element(By.ID,'fileFormatId')).select_by_value('csv')

#點選○進階下載
driver.find_element(By.CSS_SELECTOR, 'input#downloadTypeId2').click()

sleep(1)

#點選想要的縣市 「台北A，新北F，桃園H，台中B，高雄E」
city_list = ['A', 'F', 'H', 'B', 'E']

for i in city_list:    
    driver.find_element(By.CSS_SELECTOR, f"input[value = '{i}_lvr_land_A']").click()

#點選下載按鈕
download_button = driver.find_element(By.CSS_SELECTOR, 'input#downloadBtnId')
download_button.click()

sleep(10)

#關閉網頁
driver.quit()

