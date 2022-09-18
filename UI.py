from tkinter import *
from tkinter import ttk
import keyboard as k
from tkinter import Text

import random


root = Tk()
width,height = root.winfo_screenwidth(),root.winfo_screenheight()
canvasSize = root.geometry('%dx%d+0+0'%(width,height))
root.title('WDocProj')
root.config(background="#E4DCCF")#hex colors must have the hashtag in specifying
#root.resizable(False,False)
#root.attributes('-fullscreen',True)
frm = ttk.Frame(root,padding=10)
frm.config()
frm.place()

'''
test out core features. then move it on a separate library later
'''


#widgets goes here
navFile1 = ttk.Button(text="File")
navFile1.config()
navFile1.place(width=100,height=25,x=10,y=10)


root.mainloop()
