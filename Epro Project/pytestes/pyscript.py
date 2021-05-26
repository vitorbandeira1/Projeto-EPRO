#pip install selenium
#pip install webdriver-manager

from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
  
newUser = input("Insira usuario:")
newUsers = newUser.split(' ')
usersArmazenados = ['danielfontesm']
todosUser = newUsers + usersArmazenados
todosUser = usersArmazenados

print(todosUser)

driver = webdriver.Chrome(ChromeDriverManager().install())
  
# Usuarios que vao receber a msg
# Msg a ser enviada
message_ = ("testando GUI")
  
  
class bot:
    def __init__(self, username, password, todosUser, message):
        self.username = username
        self.password = password
        self.user = todosUser
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
  
    def login(self):
        self.bot.get(self.base_url)
        #Fazendo login
        #Usuario
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        #Senha
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        #retornando
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
  
        # Lidando 1 pop-up
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)
  
        # Lidando 2 pop-up
        self.bot.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)

            

        # entrando direct
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()  # //*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg
        time.sleep(3)
  
        # entrando msg
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()   #//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div/svg
        time.sleep(2)


        for i in todosUser:
  
            # escrevendo username
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i) 
            time.sleep(2)
  
            # clicabdo username
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div').click()
            time.sleep(2)
  
            # butao de next
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div').click()
            time.sleep(2)
  
            # clicando msg
            send = self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
  
            # escrevendo msg
            send.send_keys(self.message)
            time.sleep(1)
  
            # mandando msg
            send.send_keys(Keys.RETURN)
            time.sleep(2)
  
            self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)
  
  
def init():
    bot('vitorbandeira_', '32647022Vb', todosUser, message_)
  
    # when our program ends it will show "done".
    input("DONE")
  
  
# # calling the function
init()