#ashushua123
#1234567890b

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class BotSeguidor:
    def __init__(self):
        self.browser = Chrome()

    def login(self):
        self.browser.get('https://instagram.com')
        
        login_name = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        login_password = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
        login_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')))

        login_name.send_keys('ashushua123')
        login_password.send_keys('1234567890b')
        login_button.click()

        pu_botao1 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
        pu_botao1.click()

        pu_botao2 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')))
        pu_botao2.click()

    def follow_all(self):

        ver_perfis =  WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a')))
        ver_perfis.click()

        perfis = self.browser.find_elements_by_tag_name('button')
    
        for cada_perfil in perfis:
            cada_perfil.click()
            #html.send_keys(Keys.PAGE_DOWN)
          

for c in range(3):
    bot = BotSeguidor()
    bot.login()
    bot.follow_all()
    bot.browser.refresh()
    bot.browser.close()
    sleep(3)
