from tkinter import *
#this will be the basic utility library of the text editor

#probably like the onload command stuff for some heavy processor

class paper:

    def create_paper(x,y,resolution,canvasID):
        dimension = resolution.split("x")
        dimen = []
        for elements in dimension:
            dimen.append( int(elements))
        
        #anchor point system stuff
        #automatically creates the paper using one anchor point
        canvasID.create_rectangle(x,y,dimen[0]+0,y+dimen[1], fill="#FFFFFF",outline="#FFFFFF")

class Canvas:
    def create_canvas():
        pass

#NOTE: this will be the constant stuff:

placeholderText1 = "Type something here"

class Alignment:
    
    def center(textPad):
        
        a = textPad.get("current linestart",END)
        b = textPad.tag_ranges(SEL)
        cursor_index = textPad.index(INSERT) #index zero gets the first character of the index: line location
        if b:
            current_selection_line_index1  = textPad.index(SEL_LAST)
            current_selection_line_index2 = textPad.index(SEL_FIRST)

        if len(a) > 0 and placeholderText1 in a:
            print("placeholder text found!")
            
        elif placeholderText1 not in a and len(a)>0 and len(b)==0: #JUSTIFIES ONE LINE WHERE INSERT INDEX IS LOCATED
            textPad.tag_configure("center",justify="center")
            textPad.insert('insert linestart',"\t"*5,"center")#this works somehow:
            #all i need to add now is undoing formatting when pressing backspace 
            print(f'length of selection: {len(b)}')
            print("centered! - method 1")

        #A. If the cursor is at the last part near the last line of selection Index(from top to bottom selection)
        elif textPad.tag_ranges(SEL) and len(b) > 0 and cursor_index[0] == current_selection_line_index1[0]:#JUSTIFIES SELECTED MULTIPLE LINES
            c = textPad.get('sel.first','sel.last')

            textPad.tag_configure("center",justify="center")#get the linestart of the selection
            textPad.insert('insert linestart','\t'*5,'center')
            #[/]make and algorithm that detects the selected lines
            #[/]gets the lines selected
            #[/]create insert algorithms for each loop
            #[ ]keeps the justification when entered is pressed

            newLines = c.count('\n')
            print(f"newline counted{newLines}")

            line = 0 
            #print(c)
            while line <= newLines: #remove the selection
                
                print('newlines\n-----------')
                textPad.insert(f'insert linestart - {line} lines','\t','center')
                print('line ' +str(line))
                #print(textPad.index(SEL_FIRST))
                line +=1

            print("centered! - method 2A")
            textPad.tag_remove(SEL,'1.0',END)

        #B. If Insert Cursor is near at the first selection(selected from bottom to top)
        elif textPad.tag_ranges(SEL) and len(b) > 0 and cursor_index[0] == current_selection_line_index2[0]:
            #BUG:it aligns the character below exceeding on the selection

            c = textPad.get('sel.first','sel.last')

            textPad.tag_configure("center",justify="center")#get the linestart of the selection
            textPad.insert('insert linestart','\t'*5,'center')
            line = 0 
            
            newLines = c.count('\n')
            print(f"newline counted{newLines}")
            while line <= newLines:
            
                print('newlines\n-----------')
                print('line ' +str(line))
                textPad.insert(f'insert linestart + {line} lines','\t','center')

                line +=1

                    #print(textPad.index(SEL_FIRST))
            print("centered! - method 2B")
            textPad.tag_remove(SEL,'1.0',END)#removes selections

        else:
            print(f'length of selection: {len(b)}')    
           


        pass
    def left():
        pass
    def right():
        pass
