
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

s=Service('./firefox/geckodriver')
driver = webdriver.Firefox(service=s)

driver.get('https://lekomtsev.turbo.site/')

print('Title: %s' % driver.title)

#element = driver.find_element(Options.XPATH,"//*[@id="1691cdb1-a2fe-4485-9589-d32ae66959a2"]/div/div/div[1]/div[3]/div/div/a/span/span")
#element.click()

driver.quit()