from tkinter import *
from tkinter import ttk
import pandas as pd
from tkinter import filedialog

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
  

class Application:
    def __init__(self, master=None):
        self.usuarios = ""
        self.msg = ""

        self.fontePadrao = ("Calibri", "14", "bold")
        self.fonteSecundaria = ("Calibri", "14")

        self.paddingTop = Frame(master)
        self.paddingTop.configure(background='#3a3b3d')
        self.paddingTop.pack(padx=35,pady=35)

        self.title = Frame(master)
        self.title.pack()

        self.receptores = Frame(master)
        self.receptores.configure(background='#3a3b3d')
        self.receptores.pack()

        self.mensagem = Frame(master)
        self.mensagem.configure(background='#3a3b3d')
        self.mensagem.pack()

        self.processInput = Frame(master)
        self.processInput.pack()

        self.textTest = Frame(master)
        self.textTest.pack(padx=35,pady=35)

        self.carregaPlanilha = Frame(master)
        self.carregaPlanilha.pack()



        self.photo = PhotoImage(file='./assets/logo.png')
        self.titulo = ttk.Label(self.title, image=self.photo)
        self.titulo.configure(background='#3a3b3d')
        self.titulo.pack()

        self.nomeLabel = Label(self.receptores,text="Receptores(@'s):", font=self.fontePadrao, bg='#3a3b3d', fg='#f26c42')
        self.nomeLabel.configure(background='#3a3b3d')
        self.nomeLabel.pack(side=LEFT)
        #################################
        self.nome = Entry(self.receptores)
        self.nome["width"] = 35
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        self.senhaLabel = Label(self.mensagem, text="Mensagem:           ", font=self.fontePadrao, bg='#3a3b3d', fg='#f26c42')
        self.senhaLabel.configure(background='#3a3b3d')
        self.senhaLabel.pack(side=LEFT)
        #################################
        self.textMsg = Text(self.mensagem, wrap = WORD, font=self.fonteSecundaria, height=4)
        self.textMsg["width"] = 35
        self.textMsg.pack(padx=0,pady=35)

        self.autenticar = Button(self.processInput)
        self.autenticar["text"] = "Salvar dados"
        self.autenticar["font"] = ("Calibri", "10")
        self.autenticar["command"] = self.processaInput
        self.autenticar.pack()


        self.opcaoLabel = Label(self.textTest, text="Ou carregar as mensagens através de uma planilha:", font=self.fontePadrao, bg='#3a3b3d', fg='#f26c42')
        self.opcaoLabel.configure(background='#3a3b3d')
        self.opcaoLabel.pack()

        self.btnPlanilha = Button(self.carregaPlanilha, text='Importar arquivo Excel', command=self.extractFromXlsx, font=('Calibri', 10))
        self.btnPlanilha.pack()


    def processaInput(self):
        self.usuarios = self.nome.get()
        self.msg = self.textMsg.get("1.0","end")
        self.nome.delete(0, END)
        self.textMsg.delete("1.0","end")
        self.autenticar.quit()
    
    def extractFromXlsx(self):
        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel(import_file_path)
        self.usuarios = list(df["usuarios"])
        self.msg = list(df["mensagem"])
        print (self.usuarios)
        print (self.msg)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
class bot:
    def composeDict(self, usernames, message):
        dataAll = usernames + message
        dicData = {}
        m = 0
        metadeCount=int(len(dataAll)/2)
        while m < metadeCount:
            user = dataAll[m]
            msg = dataAll[m+metadeCount]
            dicData[user]=msg
            m+=1
        print (dicData)
        return dicData

    def __init__(self, username, password, todosUser, message):
        if type(todosUser) is list and type(message) is list:
            self.user = todosUser
            self.message = message
            self.username = username
            self.password = password
            self.base_url = 'https://www.instagram.com/'
            self.bot = driver
            self.dicData = self.composeDict(self.user,self.message)
            self.loginPlanilha(self.dicData)

        else:
            self.user = todosUser
            self.message = message
            self.username = username
            self.password = password
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

    def loginPlanilha(self, dicData):
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
        for k,v in dicData.items():
            # escrevendo username
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(k) 
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
            send.send_keys(v)
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
  
root = Tk()
root.geometry('600x640')
root.title('EPRO Consultoria - Instagram Bot')
root.configure(background='#3a3b3d')
A=Application(root)
root.mainloop()


if A.usuarios != "" and A.msg != "":
    if type(A.usuarios) is list and type(A.msg) is list:
        print('valores provenientes da planilha')
        todosUser = A.usuarios
        message_ = A.msg

        print(todosUser)
        print(message_)

        driver = webdriver.Chrome(ChromeDriverManager().install())
        init()

    else:
        if len(A.usuarios) > 1:
            newUsers = A.usuarios
        else:
            newUser = A.usuarios
            newUsers = newUser.split(' ')
        todosUser = newUsers
        message_ = A.msg

        print(todosUser)
        print(message_)

        driver = webdriver.Chrome(ChromeDriverManager().install())
        init()
