from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.find_element_by_css_selector('#searchInput').send_keys('List of popes')
driver.find_element_by_css_selector('#searchInput').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('#mw-content-text > div > div:nth-child(13) > table > tbody > tr:nth-child(4) > td:nth-child(4) > b > a').send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//table//a[text()="Anacletus"]').send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//a[contains(text(), "Anacletus")]').send_keys(Keys.ENTER)
#driver.find_element_by_css_selector('a:contains("Anacletus")').send_keys(Keys.ENTER)
assert driver.find_element_by_xpath('//span[contains(text(), "Anacletus")]')
#assert driver.find_element_by_css_selector('span:contains("Anacletus")')
driver.quit()