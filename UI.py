from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Button,Combobox,Menubutton
from tkinter import Canvas 
from PIL import Image, ImageTk

#IMPORTANT NOTE: ADD REPLACE THE PLACE WITH PACK INSTEAD PARA SA SCROLLBAR

#INCLUDE BASIC COLORS FOR REUSABILITY
Green1 = "#1C6758"
Green2 = "#3D8361"
Beige1 = "#D6CDA4"

#import random
root = Tk()
width,height = root.winfo_screenwidth(),(root.winfo_screenheight()+1000)
canvasSize = root.geometry('%dx%d+0+0'%(width,height))
root.title('FleetFiddle')
#root.config(background="cyan")
#hex colors must have the hashtag in specifying
root.state('zoomed')
#MAIN FRAME
frm = ttk.Frame(root,padding=0)
frm.pack()

paper_height = 50000


'''  test out core features. then move it on a separate library later   '''

paperframe = ttk.Frame(frm,width=1000,height=1000,padding=0)
paperframe.pack(pady=(100,0))

#other window aspect
paperBg = Canvas(paperframe,width=10000,height=1000,background=Beige1,highlightthickness=0,bd=0,relief="ridge")
paperBg.config(scrollregion=(0,0,10000,10000))
paperBg.pack(fill=NONE,side=TOP)

#make class for paper resolutions later
a1= [2480,3508]
tst = [1160,2300]

paper_res = tst #replace array to dynamically change page resolution

'''you can place the widgets on canvas using create_window, figure it out'''
paper1 = paperBg.create_rectangle(paper_res[0],paper_res[1],270,100,fill="#FFFFFF",outline="#FFFFFF")



canvas = Canvas(root,width=10000,height=130,background=Green1,highlightthickness=0,bd=0,relief="ridge",state=NORMAL)
canvas.place(x=0,y=0)
#canvas.create_rectangle(10000,80,0,80,outline=Beige1,width=2,activefill=Green2)

canvas2 = Canvas(canvas,width=10000,height=50,background=Green2,highlightthickness=0,bd=0,relief="ridge")
canvas2.place(x=0,y=80)
canvas2.create_rectangle(10000,60,-10,0,outline=Beige1,width=5)

canvas3 = Canvas(frm,width=70,height=1000,background=Green2,highlightthickness=0,bd=0,relief="ridge")
canvas3.place(x=0,y=80)


class docnameReg:
    placeholderText2 = " Untitled"
    def removeFocus(event): 
        a =Docname.get()
        if event:
            root.focus()
            Docname.config(bd=0,highlightthickness=0)
            #It also needs to autoselect upon clicking
            if len(Docname.get())  == 0 and docnameReg.placeholderText2 not in a:#needs to detect empty strings
                Docname.delete(0,END)
                Docname.config(fg="grey",font=("calibri",22,"bold","italic"))
                Docname.insert(0,docnameReg.placeholderText2)

            elif len(Docname.get()) > 0 and docnameReg.placeholderText2 not in a and " " in a[0:4]:
                if " " in a[0:4]: #can be optimize to shorter I think
                    empty = False #default value for the empty string
                    for chr in a[0:6]:
                        match chr:
                            case " ":
                                empty = True
                                print(empty)#temporary feedback. remove later
                            case _:
                                empty = False
                                break

                    if empty:
                        docnameReg.insertplaceholdertext()
                        Docname.config(fg=Beige1)

                else:
                    docnameReg.insertplaceholdertext()

    def insertplaceholdertext():
        Docname.delete(0,END)
        Docname.config(fg="grey",font=("calibri",22,"bold"))
        Docname.insert(0,docnameReg.placeholderText2)

#-----------------------------------------------
    def active(event):
        a =Docname.get()#fix this one later
        if event:
            Docname.config(bd=1)
            Docname.config(fg=Beige1,font=("calibri",22,"bold","roman"))#roman for unslanted
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

class popUps:
    def popN1():
        pop1 = Toplevel(root)
        pop1.geometry('800x450')
        pop1.title('OpenFile')
        x = root.winfo_x()
        y = root.winfo_y()
        pop1.geometry("+%d+%d" %(x+300,y+180))


navFile1 = Menubutton(text="File",style='Nav.TButton',takefocus=False)
navFile1.config()
navFile1.place(width=75,height=23,x=35,y=nav_y)
navFile1.menu = Menu(navFile1,tearoff=0) #tearoffs might be essential when we make more options
navFile1["menu"] = navFile1.menu
#nonfunctional options so far
navFile1.menu.add_command(label="Open File",command=popUps.popN1)
navFile1.menu.add_command(label="Save As")
navFile1.menu.add_command(label="Print")
navFile1.menu.add_command(label="Preferences")
navFile1.menu.add_command(label="Document Details")

navFile2 = Button(text="Edit",style='Nav.TButton',takefocus=False)
#replace this widget with menu button and remove Topwidgets
navFile2.config ()
navFile2.place(width=75,height=23,x=(75+35+2),y=nav_y)


navFile3 = Button(text="Insert",style='Nav.TButton',takefocus=False)
navFile3.config()
navFile3.place(width=75,height=23,x=((75*2)+35+ 4),y=nav_y)

navFile4 = Button(text="View",style='Nav.TButton',takefocus=False)
navFile4.config()
navFile4.place(width=75,height=23,x=((75*3)+35+ 6),y=nav_y)
#pop widgets goes here 


#SCROLLBAR Feature for page navigation
'''Scrollbar'''
pageScrollbar = Scrollbar(paperframe,orient=VERTICAL,command=paperBg.yview)
pageScrollbar.place(x=1345,y=28,height=580)

paperBg.config(yscrollcommand=pageScrollbar.set)


                    #CONTENT UTILITIES

#1. the font alignment buttons (left,centered, right)
class Alignment_F:
    '''
        Alignment Functions:
        -left align either(add no tab spaces, or remove tabs spaces when the line is currently
        on center or right align)
        -center Align removes or remove tab spaces depends on left or right alignment
        -right Align adds tab spaces or mirror the index of start type oringin to the right and slide to left upon editing

        REstraints: it must not modify placeholder text in textpad

        In text Indexing use 'Insert' instead of 'Current'

    '''
    #Alignment functions goes here (the ff are beta features improve na lang to)
    def center():
       
        a = textpad.get("current linestart",END)
        if len(a) > 0 and placeholderText1 in a:
            print("placeholder text found!")
            
        else:
            textpad.tag_configure("center",justify="center")
            textpad.insert('insert linestart',"\t"*5,"center")#this works somehow:
            #all i need to add now is undoing formatting when pressing backspace 
            
            print("centered!")
    def left():#it deletes the the text in the line
        a = textpad.get("insert linestart",'insert lineend')
        #GET THE INDEX OF NON SPACE
        
        lineLength = str(len(a))
        print(f'line length{lineLength}')

        replChr = 0
        for characters in a: #has to count the spaces in the insert
            if characters.isspace() == FALSE:
                replChr +=1
            if characters.isspace() and characters != "\t": #gives exception to tab spaces
                replChr +=1
        textpad.delete('insert linestart',f'insert - {replChr} chars')
        print(f"replChr: {replChr}") #has an error if sentence has spaces of not indentation

        textpad.tag_configure("left",justify="left")
        
        print("align-left")
        



class Alignment_widget:

    alignment_y = 92 #base y alignment
    alignment_label = Label(text="Alignment:").place(x=845,y=(alignment_y - 20))
    bt_aspr = 30
    img_aspr = 28 #image aspect ratio

    #Button style
    alBtn = ttk.Style()
    alBtn.theme_use("default")
    alBtn.configure("A.TButton",relief=FLAT,background=Beige1,padding=0)
    alBtn.map("A.TButton",background = [('active', Beige1)])


    #left align btn
    l_img = Image.open("Icons\Left_icon.png")
    r_l_img = l_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    L_img = ImageTk.PhotoImage(r_l_img)

    AL_x = 830
    L_allignment = Button(text="",image=L_img,compound=TOP,takefocus=False,style="A.TButton") #worked now. need it to fit in btn
    L_allignment.place(x=AL_x,y=alignment_y,width=bt_aspr,height=bt_aspr) 
    L_allignment.config(command=Alignment_F.left)

    #center align btn
    c_img = Image.open("Icons\Center_icon.png")
    r_c_img = c_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    C_img = ImageTk.PhotoImage(r_c_img)

    AL_x2 = AL_x+bt_aspr+2
    C_allignment = Button(root,text='',image=C_img,compound=TOP,takefocus=False,style="A.TButton") #maybe replace it with icons later on
    C_allignment.config(command=Alignment_F.center)
    C_allignment.place(x=AL_x2,y=alignment_y,width=bt_aspr,height=bt_aspr)

    #right align btn
    r_img = Image.open("Icons\Right_icon.png")
    r_r_img = r_img.resize((img_aspr,img_aspr), Image.Resampling.LANCZOS)
    R_img = ImageTk.PhotoImage(r_r_img)
    AL_x3 = AL_x2 + bt_aspr +2
    R_allignment = Button(text='',image=R_img,compound=TOP,takefocus=False,style="A.TButton") #maybe replace it with icons later on
    R_allignment.place(x=AL_x3,y=alignment_y,width=bt_aspr,height=bt_aspr)

class fontSizeTools:
    #2. the font Size field and fixed size buttons
    bt_y = (Alignment_widget.alignment_y + 4)
    Fz_btnW,Fz_BtnH = 20,20
    field_x = 600
    iconSize = 20

    Label2 = Label(text="Font Size:").place(x=580,y=(bt_y-22),width=58,height=20)
    Fz_Field = Entry()
    Fz_Field.config(bg=Beige1,font=("Arial",10,"bold"),fg=Green1,justify="center",bd=0)
    Fz_Field.insert(0,"12")
    Fz_Field.place(x=field_x,y=bt_y,width=30,height=20)
    #ICONS
    pl_img = Image.open("Icons\plusIC.png")
    r_pl_img = pl_img.resize((iconSize,iconSize), Image.Resampling.LANCZOS)
    PLs_img = ImageTk.PhotoImage(r_pl_img)

    mn_img = Image.open("Icons\minusIC.png")
    mn_pl_img = mn_img.resize((iconSize,iconSize), Image.Resampling.LANCZOS)
    MNs_img = ImageTk.PhotoImage(mn_pl_img)


    addFontSize = Button(image=PLs_img,takefocus=False,style="A.TButton")
    
    addFontSize.place(x=(field_x +Fz_btnW+9),y=bt_y,width=Fz_btnW,height=Fz_BtnH,bordermode='inside')

    decreaseFontSize = Button(compound=CENTER,image=MNs_img,takefocus=False,style="A.TButton")
    decreaseFontSize.place(x=(field_x-Fz_btnW),y=bt_y,width=Fz_btnW,height=Fz_BtnH,bordermode='inside')

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
            #print(event)
            textpad.insert(END,placeholderText1)
            textpad.config(font=("calibri",12,"italic"),fg="#808080")
            root.focus()

#this class is disposeable
   
p_label = Label(paperframe,text="paper_page_1",bg="grey")
p_label.place(x=270,y=160)
#add separate class here later

#text field goes here(textpad needs to scroll along with the canvas)
placeholderText1 = "Type something here" # << BUG FOUND
textpad = Text(paperframe)
textpad.config(bd=0,font=("calibri",11,"italic"),fg="#808080")
textpad.place(x=0,y=0,width=750,height=1500)
textpad.insert(END,placeholderText1)
#x=350,y=(100+130)
textpad.bind('<FocusIn>',emptyDocCont.deletePlaceholderText)
textpad.bind('<Leave>',emptyDocCont.insertPlaceholderText) #or use '<FocusOut>' here

textpad.see(END)

#instead of clipping one widget, it has to clip a frame I guess?
tpl_window = paperBg.create_window((270,80),anchor='nw',window=p_label)
tp_window = paperBg.create_window((350,230),anchor='nw',width=750,height=1500,window=textpad)


root.mainloop()
