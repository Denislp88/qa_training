
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./firefox/geckodriver")
browser.get('https://kcentr.ru/')

print('Title: %s' % browser.title)
#browser.quit()  пока не используем