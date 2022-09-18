from tkinter import *
from tkinter import ttk
import keyboard as k
from tkinter import Text,Canvas


#import random


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

#other window aspect
canvas = Canvas(root,width=10000,height=45,background="#576F72",highlightthickness=0,bd=0,relief="ridge")
canvas.place(x=0,y=0)

paperplace = Canvas(root,width=1000,height=2000,background="#FFFFFF",highlightthickness=0,bd=0,relief="ridge")
paperplace.place(x=250,y=50)


#widgets goes here
navFile1 = ttk.Button(text="File",)
navFile1.config()
navFile1.place(width=85,height=23,x=10,y=10,bordermode="inside")

textpad = Text()
textpad.place(x=300,y=100,width=800,height=1500)

root.mainloop()
