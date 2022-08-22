
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="./firefox/geckodriver")
driver.get('https://lekomtsev.turbo.site/')

print('Title: %s' % driver.title)

driver.quit()