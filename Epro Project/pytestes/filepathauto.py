from tkinter import filedialog

from tkinter import *

import os, sys

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = os.getcwd(),filetypes = [('image files', '.png')])
imageR = root.filename
print(imageR)