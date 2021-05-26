#pip install openpyxl
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    print (df)
    
browseButton_Excel = tk.Button(text='Importar arquivo Excel', command=getExcel, font=('Calibri', 10))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()




















# from tkinter import ttk
# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText


# def demo():
#     root = tk.Tk()
#     root.title("ttk.Notebook")

#     # mensagem = Frame(root)
#     # mensagem.configure(background='#3a3b3d')
#     # mensagem.pack()


#     nb = ttk.Notebook(root)

#     # adding Frames as pages for the ttk.Notebook 
#     # first page, which would get widgets gridded into it
    
#     page1 = ttk.Frame(nb)
#     page2 = ttk.Frame(nb)
    
#     text = ScrolledText(page2)
#     text.pack(expand=1, fill="both")

#     nb.add(page1, text='One')

#     senhaLabel = ttk.Label(page1, text="Mensagem")
#     senhaLabel.configure(background='#3a3b3d')
#     senhaLabel.pack()
#     # #################################
#     # textMsg = ttk.Text(page1)
#     # textMsg["width"] = 35
#     # textMsg.pack(padx=0,pady=35)

#     nb.add(page2, text='Two')

#     nb.pack(expand=1, fill="both")

#     root.mainloop()

# if __name__ == "__main__":
#     demo()


# from tkinter import *
# master = Tk()

# def var_states():
#    print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

# Label(master, text="Your sex:").grid(row=0, sticky=W)
# var1 = IntVar()

# Checkbutton(master, text="Escrever", variable=var1).grid(row=1, sticky=W)
# var2 = IntVar()

# Checkbutton(master, text="Puxar de planilha", variable=var2).grid(row=1, column=2, sticky=W)
# Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
# Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
# mainloop()



# from tkinter import *
# from tkinter.ttk import *

# window = Tk()
# window.title("Welcome to LikeGeeks app")
# window.geometry('350x200')

# def var_states():
#     select1 = var1.get()
#     if select1 == 1:
#         print('Opcao 1')
#     elif  select1 == 2:
#         print('Opcao 2')
#     else:
#         print('Opcao 3')

# var1 = IntVar()

# rad1 = Radiobutton(window,text='First', value=1,variable=var1)
# rad2 = Radiobutton(window,text='Second', value=2,variable=var1)
# rad3 = Radiobutton(window,text='Third', value=3,variable=var1)

# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)

# Button(window, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

# window.mainloop()



# import tkinter as tk                    
# from tkinter import ttk
  
  
# root = tk.Tk()
# root.title("Tab Widget")
# tabControl = ttk.Notebook(root)
  
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
  
# tabControl.add(tab1, text ='Tab 1')
# tabControl.add(tab2, text ='Tab 2')
# tabControl.pack(expand = 1, fill ="both")
  
# ttk.Label(tab1, 
#           text ="Welcome to \
#           GeeksForGeeks").grid(column = 0, 
#                                row = 0,
#                                padx = 30,
#                                pady = 30)  
# ttk.Label(tab2,
#           text ="Lets dive into the\
#           world of computers").grid(column = 0,
#                                     row = 0, 
#                                     padx = 30,
#                                     pady = 30)
  
# root.mainloop() 