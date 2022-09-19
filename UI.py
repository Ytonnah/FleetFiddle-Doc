from tkinter import *
from tkinter.ttk import *
from tkinter import Text,Canvas
#import time
#import keyboard
#import os

#import random
root = Tk()
width,height = root.winfo_screenwidth(),root.winfo_screenheight()
canvasSize = root.geometry('%dx%d+0+0'%(width,height))
root.title('WDocProj')
root.config(background="#E4DCCF")#hex colors must have the hashtag in specifying
#root.resizable(False,False)
#root.attributes('-fullscreen',True)
frm = Frame(root,padding=10)
frm.place()

#initializing frames for each button trigger signals
s = Style()
s.configure("My.TFrame",background="red")

edit = Frame(root,padding=10,style="My.TFrame")
edit.config()#make it so the the widget frame display is hidden
#edit.place(x= 10,y=20,width=50,height=100)


'''
test out core features. then move it on a separate library later
'''
#functionalities
class liner:
    linecounter = 0#linecounted should be part of the method
    def addCodeLine(event):
    
        linecounter+=1
        #print("beep")
        #a =  str(linecounter) + '\t\n'
        a = "something \n"
        textpad.insert(END,a)
        
        #time.sleep(5)

class TopWidgets:
    def show():edit.place(x= 10,y=20,width=50,height=100)#reseting the plcement
    hidden = False
    def hide():
        if TopWidgets.hidden == False: #I need to think of a better popup mechanics
            edit.place_forget()
            navFile2.configure(command=TopWidgets.show)
            TopWidgets.hidden = True#its closing and re placing now. all I need is to make it appear everytime it is clicked
        else:
            TopWidgets.show()
            navFile2.configure(command=edit.place_forget)
            TopWidgets.hidden = False

        

def maincommand(a):
    liner.addCodeLine(a)

#other window aspect
canvas = Canvas(root,width=10000,height=45,background="#576F72",highlightthickness=0,bd=0,relief="ridge")
canvas.place(x=0,y=0)
canvas2 = Canvas(root,width=10000,height=45,background="#3D8361",highlightthickness=0,bd=0,relief="ridge")
canvas2.place(x=0,y=45)


paperplace = Canvas(root,width=1000,height=2000,background="#FFFFFF",highlightthickness=0,bd=0,relief="ridge")
paperplace.place(x=250,y=150)


#widgets goes here
style1 = Style()
style1.configure('Custom.TButton',font=("calibri",11),background="#7D9D9C")

#very top nav bar goes here
navFile1 = Button(text="File",style='Custom.TButton')
navFile1.config()
navFile1.place(width=75,height=23,x=10,y=6)

navFile2 = Button(text="Edit",style='Custom.TButton',command=TopWidgets.hide)
navFile2.place(width=75,height=23,x=100,y=6)
#navFile2.bind('<Button-1>',TopWidgets.openFileBtn)
#word editing utilities goes here.

edit.place(x= 10,y=20,width=50,height=100)


#text field goes here
textpad = Text(bd=0)
#textpad.insert(END,"0\t")
textpad.config(font=("calibri",12))
textpad.place(x=350,y=200,width=800,height=1500)
#textpad.bind('<Return>',maincommand)

root.mainloop()
