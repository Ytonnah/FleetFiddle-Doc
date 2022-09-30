from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Button,Combobox,Menubutton
from tkinter import Canvas 
from PIL import Image, ImageTk


#INCLUDE BASIC COLORS FOR REUSABILITY
Green1 = "#1C6758"
Green2 = "#3D8361"
Beige1 = "#D6CDA4"

#import random
root = Tk()
width,height = root.winfo_screenwidth(),(root.winfo_screenheight()+1000)
canvasSize = root.geometry('%dx%d+0+0'%(width,height))
root.title('FleetFiddle')
root.config(background="cyan")#hex colors must have the hashtag in specifying
#root.resizable(False,False)
#root.attributes('-fullscreen',True)
root.state('zoomed')#this work
#MAIN FRAME
frm = ttk.Frame(root,padding=0)
frm.place()

#implementation of color scheme goes here

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
paperBg = Canvas(root,width=10000,height=5000,background=Beige1,highlightthickness=0,bd=0,relief="ridge")
paperBg.place(x=0,y=130)

canvas = Canvas(root,width=10000,height=80,background=Green1,highlightthickness=0,bd=0,relief="ridge")
canvas.place(x=0,y=0)
canvas2 = Canvas(root,width=10000,height=50,background="#3D8361",highlightthickness=0,bd=0,relief="ridge")
canvas2.place(x=0,y=80)
canvas2.create_rectangle(10000,60,-10,0,outline=Beige1,width=5)

paper_y = 250
paperplace = Canvas(root,width=1000,height=2000,background="#FFFFFF",highlightthickness=0,bd=0,relief="ridge")
paperplace.place(x=250,y=paper_y)




#registered name of Document goes here:
class docnameReg:
    placeholderText2 = " Untitled"
    def removeFocus(event): 
        a =Docname.get()
        if event:
            root.focus()
            Docname.config(bd=0)
            #It also needs to autoselect upon clicking
            if len(Docname.get())  == 0 and docnameReg.placeholderText2 not in a:#needs to detect empty strings
                #Docname.config(fg="red")
                Docname.delete(0,END)
                Docname.config(fg="grey",font=("calibri",22,"bold"))
                Docname.insert(0,docnameReg.placeholderText2)
            elif len(Docname.get()) > 1 and docnameReg.placeholderText2 not in a and a[0:5] == " ":
                # has to give exeption on names with spaces
                Docname.delete(0,END)
                Docname.config(fg="grey",font=("calibri",22,"bold"))
                Docname.insert(0,docnameReg.placeholderText2)
            else:
                pass
                
            Docname.config(fg=Beige1)

            
    def active(event):
        a =Docname.get()#fix this one later
        if event:
            Docname.config(bd=1)
            Docname.selection_range(0,END)
            if a[0]!=" ":
                Docname.insert(0," ")


Docname = Entry(root)
Docname.config(bg=Green1,font=("calibri",22,"bold"),fg=Beige1,bd=0,justify="left")
Docname.place(x=45,y=13,width=500,height=30)
Docname.insert(END,"Document")
Docname.bind('<FocusIn>',docnameReg.active)#this one works well
Docname.bind('<FocusOut>',docnameReg.removeFocus)#trial Bind Widget


#NAVIGATION AND ESSENTIALS (note: use menu button widgets instead)
style1 = ttk.Style()
style1.theme_use("default")
style1.configure('Nav.TButton',font=("calibri",11,"bold"),relief="flat",background=Beige1,foreground=Green1)
style1.map('Nav.TButton',background =[('active',Beige1)])
#add stying for menubutton

nav_y = 58 #the y-axis of the navigation widget is just the same

navFile1 = Menubutton(text="File",style='Nav.TButton',takefocus=False)
navFile1.config()
navFile1.place(width=75,height=23,x=35,y=nav_y)
navFile1.menu = Menu(navFile1)
navFile1["menu"] = navFile1.menu
#nonfunctional options so far
navFile1.menu.add_command(label="Open File")
navFile1.menu.add_command(label="Save As")
navFile1.menu.add_command(label="Print")

navFile2 = Button(text="Edit",style='Nav.TButton',takefocus=False)
navFile2.config (command=TopWidgets.show)
navFile2.place(width=75,height=23,x=(75+35+2),y=nav_y)
#navFile2.bind('<Button-1>',TopWidgets.openFileBtn)
#word editing utilities goes here.

navFile3 = Button(text="Insert",style='Nav.TButton',takefocus=False)
navFile3.config()
navFile3.place(width=75,height=23,x=((75*2)+35+ 4),y=nav_y)

navFile4 = Button(text="View",style='Nav.TButton',takefocus=False)
navFile4.config()
navFile4.place(width=75,height=23,x=((75*3)+35+ 6),y=nav_y)
#pop widgets goes here 
edit = Frame(root)
edit.config()#make it so the the widget frame display is hidden
edit.place_forget()


#SCROLLBAR Feature for page navigation
pageScrollbar = Scrollbar(orient=VERTICAL,command=paperBg.yview)
pageScrollbar.place(x=1345,y=130,height=10000)

paperBg.config(yscrollcommand=pageScrollbar.set)
paperBg.bind('<Configure>',lambda e: paperBg.configure(scrollregion=paperBg.bbox("all")))

pbg2 = Frame(paperBg)
paperBg.create_window((0,0),window=pbg2,anchor="nw")
'''
Scroll Feature needs rework
---------------------------
there is hard to implement the feature


'''
#Add the content tools bar(below the nav bars)

#1. the font alignment buttons (left,centered, right)
class Alignment_F:
    '''
        Alignment Functions:
        -left align either(add no tab spaces, or remove tabs spaces when the line is currently
        on center or right align)
        -center Align removes or remove tab spaces depends on left or right alignment
        -right Align adds tab spaces or mirror the index of start type oringin to the right and slide to left upon editing

        REstraints: it must not modify placeholder text in textpad

    '''
    #Alignment functions goes here (the ff are beta features improve na lang to)
    def center():
        #add event binds later
        a = textpad.get("1.0","1.22")
        if a == placeholderText1:
            print("placeholder text found!")
        else:
            textpad.insert("0.0","\t\t\t\t\t.")
            #textpad.config("lineTEST",justify="center")
            print("beep")
    def left():#it deletes the the text in the line
        a = textpad.get("1.0","1.22")
        if a == placeholderText1:
            print("ops")
        else:
            textpad.delete("0.0",END)


class Alignment_widget:

    alignment_y = 92 #base y alignment
    alignment_label = Label(text="Alignment:").place(x=845,y=(alignment_y - 20))
    bt_aspr = 30
    img_aspr = 30 #image aspect ratio

    alBtn = ttk.Style()
    alBtn.theme_use("default")
    alBtn.configure("A.TButton",relief="flat",background="#3D8361",padding=0)
    alBtn.map("A.TButton",background = [('active', "#3D8361")])
    #left align btn
    l_img = Image.open("Icons\Left_icon.png")
    r_l_img = l_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    L_img = ImageTk.PhotoImage(r_l_img)

    AL_x = 830
    L_allignment = Button(text="",image=L_img,compound="center",takefocus=False,style="A.TButton") #worked now. need it to fit in btn
    L_allignment.place(x=AL_x,y=alignment_y,width=bt_aspr,height=bt_aspr) 
    L_allignment.config(command=Alignment_F.left)

    #center align btn
    c_img = Image.open("Icons\Center_icon.png")
    r_c_img = c_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    C_img = ImageTk.PhotoImage(r_c_img)

    AL_x2 = AL_x+bt_aspr+2
    C_allignment = Button(root,text='',image=C_img,compound="center",takefocus=False,style="A.TButton") #maybe replace it with icons later on
    C_allignment.config(command=Alignment_F.center)
    C_allignment.place(x=AL_x2,y=alignment_y,width=bt_aspr,height=bt_aspr)

    #right align btn
    r_img = Image.open("Icons\Right_icon.png")
    r_r_img = r_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    R_img = ImageTk.PhotoImage(r_r_img)
    AL_x3 = AL_x2 + bt_aspr +2
    R_allignment = Button(text='',image=R_img,compound="right",takefocus=False,style="A.TButton") #maybe replace it with icons later on
    R_allignment.place(x=AL_x3,y=alignment_y,width=bt_aspr,height=bt_aspr)

class fontSizeTools:
    #2. the font Size field and fixed size buttons
    bt_y = (Alignment_widget.alignment_y + 4)
    Fz_btnW,Fz_BtnH = 20,20
    field_x = 600
    iconSize = 20

    Label2 = Label(text="Font Size:").place(x=580,y=(bt_y-22),width=55,height=20)
    Fz_Field = Entry()
    Fz_Field.insert(0,"12")
    Fz_Field.place(x=field_x,y=bt_y,width=25,height=20)
    #ICONS
    pl_img = Image.open("Icons\plusIC.png")
    r_pl_img = pl_img.resize((iconSize,iconSize), Image.Resampling.LANCZOS)
    PLs_img = ImageTk.PhotoImage(r_pl_img)

    mn_img = Image.open("Icons\minusIC.png")
    mn_pl_img = mn_img.resize((iconSize,iconSize), Image.Resampling.LANCZOS)
    MNs_img = ImageTk.PhotoImage(mn_pl_img)


    addFontSize = Button(compound=CENTER,image=PLs_img,takefocus=False,style="A.TButton")
    addFontSize.place(x=(field_x +Fz_btnW+6),y=bt_y,width=Fz_btnW,height=Fz_BtnH)
    decreaseFontSize = Button(compound=CENTER,image=MNs_img,takefocus=False,style="A.TButton")
    decreaseFontSize.place(x=(field_x-Fz_btnW),y=bt_y,width=Fz_btnW,height=Fz_BtnH)

class fontStyleSelection:
    #add styling here
    fstyle = Combobox() #disable the highlight
    fstyle.insert(END,"Calibri") 
    fstyle.place(y =Alignment_widget.alignment_y,x=490,width= 80,height=25)
    fstyle['values'] = ["Default","Default2","Default3"]
    fstyle['state'] = 'readonly'




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
            print(event)
            textpad.insert(END,placeholderText1)
            textpad.config(font=("calibri",12,"italic"),fg="#808080")
            root.focus()
        

        

#text field goes here
placeholderText1 = "Type something here"
textpad = Text(bd=0)
textpad.config(font=("calibri",11,"italic"),fg="#808080")
textpad.place(x=350,y=(paper_y+130),width=800,height=1500)
textpad.insert(END,placeholderText1)
textpad.tag_configure("lineTEST",justify="left")
textpad.tag_add("lineTEST","1.0",END)
textpad.bind('<FocusIn>',emptyDocCont.deletePlaceholderText)
#textpad.bind('<FocusOut>',emptyDocCont.insertPlaceholderText)
textpad.bind('<Leave>',emptyDocCont.insertPlaceholderText)



root.mainloop()
