from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

browser = Chrome()

browser.get('https://youtube.com')

for c in range(3):
    html = browser.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)