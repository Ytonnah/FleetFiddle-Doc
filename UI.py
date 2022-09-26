from tkinter import *
from tkinter.ttk import *
from tkinter import Text,Canvas
from PIL import Image, ImageTk
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
#MAIN FRAME
frm = Frame(root,padding=0)
frm.place()

#WIDGET STYLE SETUP GOES HERE
s = Style()
s.configure("My.TFrame",background="red")


'''
test out core features. then move it on a separate library later
'''

class TopWidgets:
    def show():
        edit.place(x= 90,y=80,width=75,height=300)#reseting the plcement
        navFile2.config(command=TopWidgets.hide)
    def hide():
        edit.place_forget()
        navFile2.config(command=TopWidgets.show)


#other window aspect
canvas = Canvas(root,width=10000,height=80,background="#576F72",highlightthickness=0,bd=0,relief="ridge")
canvas.place(x=0,y=0)
canvas2 = Canvas(root,width=10000,height=50,background="#3D8361",highlightthickness=0,bd=0,relief="ridge")
canvas2.place(x=0,y=80)

paper_y = 250
paperplace = Canvas(root,width=1000,height=2000,background="#FFFFFF",highlightthickness=0,bd=0,relief="ridge")
paperplace.place(x=250,y=paper_y)


#widgets goes here
style1 = Style()
style1.configure('Custom.TButton',font=("calibri",11),background="#576F72")

#registered name of Document goes here:
DocnameS = Style()
DocnameS.configure('DcS.TEntry',bg="red",font=("calibri",30))#ISSUE: style does not apply on the entry widget.

Docname = Entry(root,style='DcS.TEntry')
Docname.place(x=10,y=13,width=250,height=30)
Docname.insert(END,"   Document")


#very top nav bar goes here
nav_y = 50
navFile1 = Button(text="File",style='Custom.TButton')
navFile1.config()
navFile1.place(width=75,height=23,x=10,y=nav_y)

navFile2 = Button(text="Edit",style='Custom.TButton')
navFile2.config (command=TopWidgets.show)
navFile2.place(width=75,height=23,x=90,y=nav_y)
#navFile2.bind('<Button-1>',TopWidgets.openFileBtn)
#word editing utilities goes here.


#pop widgets goes here 
edit = Frame(root,padding=10,style="My.TFrame")
edit.config()#make it so the the widget frame display is hidden
#edit.place(x= 10,y=20,width=50,height=100)
edit.place_forget()

#Add the content tools bar(below the nav bars)


#1. the font alignment buttons (left,centered, right)
class Alignment_tools:

    alignment_y = 87 #base y alignment
    alignment_label = Label(text="Alignment:").place(x=845,y=(alignment_y - 20))
    bt_aspr = 30
    img_aspr = 30 #image aspect ratio

    alBtn = Style()
    alBtn.theme_use("default")
    alBtn.configure("A.TButton",relief="flat",background="#3D8361",padding=0)
    alBtn.map("A.TButton",background = [('active', "#3D8361")])
    #left align btn
    l_img = Image.open("Icons\Left_icon.png")
    r_l_img = l_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    L_img = ImageTk.PhotoImage(r_l_img)

    AL_x = 830
    L_allignment = Button(text="",image=L_img,compound="center",style="A.TButton",takefocus=False) #worked now. need it to fit in btn
    L_allignment.place(x=AL_x,y=alignment_y,width=bt_aspr,height=bt_aspr) 

    #center align btn
    c_img = Image.open("Icons\Center_icon.png")
    r_c_img = c_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    C_img = ImageTk.PhotoImage(r_c_img)

    AL_x2 = AL_x+bt_aspr+2
    C_allignment = Button(root,text='',image=C_img,compound="center",style="A.TButton",takefocus=False) #maybe replace it with icons later on
    C_allignment.place(x=AL_x2,y=alignment_y,width=bt_aspr,height=bt_aspr)

    #right align btn
    r_img = Image.open("Icons\Right_icon.png")
    r_r_img = r_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    R_img = ImageTk.PhotoImage(r_r_img)
    AL_x3 = AL_x2 + bt_aspr +2
    R_allignment = Button(text='',image=R_img,compound="center",style="A.TButton",takefocus=False) #maybe replace it with icons later on
    R_allignment.place(x=AL_x3,y=alignment_y,width=bt_aspr,height=bt_aspr)

class fontSizeTools:
    #2. the font Size field and fixed size buttons
    bt_y = 90
    Fz_btnW,Fz_BtnH = 20,20
    field_x = 600

    Label2 = Label(text="Font Size:").place(x=580,y=(bt_y-22),width=55,height=20)
    Fz_Field = Entry()
    Fz_Field.insert(0,"12")
    Fz_Field.place(x=field_x,y=bt_y,width=25,height=20)

    addFontSize = Button(text="+")
    addFontSize.place(x=(field_x +Fz_btnW+6),y=bt_y,width=Fz_btnW,height=Fz_BtnH)
    decreaseFontSize = Button(text="-")
    decreaseFontSize.place(x=(field_x-Fz_btnW),y=bt_y,width=Fz_btnW,height=Fz_BtnH)

#OPTIMIZE THIS CODE LATER
class emptyDocCont:
    def deletePlaceholderText(event):#functions that deletes the placeholder text(WORKS NOW)
        a = textpad.get("1.0","1.21")
        plcd = placeholderText1 in a
        if event and plcd:
            textpad.delete("1.0","1.21")
            textpad.config(fg="black",font="italic")
            '''
            Tkinter text indexing guide:
            text widget has index pointer system.
            "1.0" means line 1 and the 0 index character or first character
            "1.21" means line 1 character 21
            '''
    def insertPlaceholderText(event):
        a = textpad.get("0.1","1.40")
        plcd = placeholderText1 in a
        if event and plcd==False and len(a) == 0:
            textpad.insert(END,placeholderText1)
            textpad.config(font=("calibri",12,"italic"),fg="#808080")
        

#text field goes here
placeholderText1 = "Type something here"
textpad = Text(bd=0)
textpad.config(font=("calibri",12,"italic"),fg="#808080")
textpad.place(x=350,y=(paper_y+100),width=800,height=1500)
textpad.insert(END,placeholderText1)
textpad.tag_add("plc","1.0","1.10") #marker
textpad.bind('<FocusIn>',emptyDocCont.deletePlaceholderText)
textpad.bind('<FocusOut>',emptyDocCont.insertPlaceholderText)


root.mainloop()
