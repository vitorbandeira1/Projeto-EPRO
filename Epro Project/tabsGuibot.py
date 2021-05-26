from tkinter import *
from tkinter import ttk


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
        self.textTest.pack()

#--------------------------------------------------------------------------------

        self.photo = PhotoImage(file='./assets/logo.png')
        self.titulo = ttk.Label(self.title, image=self.photo)
        self.titulo.configure(background='#3a3b3d')
        self.titulo.pack()

        self.nomeLabel = Label(self.receptores,text="Receptores (@'s)", font=self.fontePadrao, bg='#3a3b3d', fg='#f26c42')
        self.nomeLabel.configure(background='#3a3b3d')
        self.nomeLabel.pack(side=LEFT)
        #################################
        self.nome = Entry(self.receptores)
        self.nome["width"] = 35
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        self.senhaLabel = Label(self.mensagem, text="Mensagem           ", font=self.fontePadrao, bg='#3a3b3d', fg='#f26c42')
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


    def processaInput(self):
        self.usuarios = self.nome.get()
        self.msg = self.textMsg.get("1.0","end")
        self.nome.delete(0, END)
        self.textMsg.delete("1.0","end")
        self.autenticar.quit()



root = Tk()
root.geometry('600x510')
root.title('EPRO Consultoria - Instagram Bot')
root.configure(background='#3a3b3d')
A=Application(root)
root.mainloop()


if A.usuarios != "" and A.msg != "":
    newUser = A.usuarios
    newUsers = newUser.split(' ')
    todosUser = newUsers
    message_ = A.msg

    print(todosUser)
    print(message_)

