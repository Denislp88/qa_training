
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('./chrome/105/chromedriver' )
driver = webdriver.Chrome(service=s)

driver.get('https://lekomtsev.turbo.site/')
print('Title: %s' % driver.title)

element = driver.find_element(By.XPATH, '//*[@id="1691cdb1-a2fe-4485-9589-d32ae66959a2"]/div/div/div[1]/div[3]/div/div/a/span/span')
element.click()

#driver.quit()