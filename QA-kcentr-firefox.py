
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./firefox/geckodriver")

browser.get('https://lekomtsev.turbo.site/')

print('Title: %s' % browser.title)

#element = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/section/div[1]/div[1]/span[2]/div/div[2]/section/div/div/div[1]/div[3]/div/div/a/span')
#element.click()



#browser.quit()