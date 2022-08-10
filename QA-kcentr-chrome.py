
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service('./chrome/chromedriver' )
driver = webdriver.Chrome(service=s)

driver.get('https://kcentr.ru/')

element = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/div/div/div/div/div[1]/a')
element.click()
element = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/div/div/div/div/div[3]/a')
element.click()
element = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/div/div/div/div/div[4]/a')
element.click()