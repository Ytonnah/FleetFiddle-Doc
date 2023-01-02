
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

class Alignment:
    def center():
        pass
    def left():
        pass
    def right():
        pass