
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./firefox/geckodriver")
browser.get('https://kcentr.ru/')

driver.get('https://kcentr.ru/')

element = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/div/div/div/div/div[1]/a')
element.click()
element = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/div/div/div/div/div[3]/a')
element.click()
element = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/div/div/div/div/div[4]/a')
element.click()

print('Title: %s' % browser.title)
#browser.quit()