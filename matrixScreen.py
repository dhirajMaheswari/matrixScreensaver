'''this code generates the matrix screen like screensaver.
   it selects 3 characters randomly from set of characters and move them
   randomly in the vertical direction.
   Dhiraj.
'''


from tkinter import *
from random import randint, sample, choice
#from math import sin,cos,tan,pi

# A class to generate characters randomly

class MatrixScreen:
    '''initialize the matrix screen
    '''
    def __init__(self, canvas, scrnwidth, scrnheight):
        self.canvas = canvas
        self.xpos = randint(0,int(scrnwidth))
        self.ypos = randint(0,int(scrnheight))
        self.xvelocity = randint(3,12)
        self.yvelocity = randint(7,18)
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        
        self.color = 'green'
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*|<>.?/[]*()-+='


    def create_code(self):
    	
        x1 = self.xpos
        y1 = self.ypos
        self.itm = self.canvas.create_text(x1,y1, text = sample(self.chars,2),
        						 fill=self.color, font=('Arial',16))
        self.itm1 = self.canvas.create_text(x1+3, y1+3, text=sample(self.chars,2),
        						fill=self.color, font=('Arial',16))

    def move_code(self):
    	
        self.ypos += self.yvelocity
        if self.ypos >= self.scrnheight or self.ypos <= 6:           
           self.ypos = randint(0,self.scrnheight)
           self.xpos = randint(0,self.scrnwidth)
           self.yvelocity = -self.yvelocity # change direction

        self.canvas.move(self.itm, 0.0, self.yvelocity)
        self.canvas.move(self.itm1, 0.0, self.yvelocity+2)
        


class ScreenSaver:
    codes = []
    
    def __init__(self, num_codes):
        self.root = Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.attributes('-alpha', 0.99)

        self.root.bind('<Any-KeyPress>', quit)
        self.root.bind('<Any-Button>', quit)
        self.root.bind('<Motion>', quit)
        self.canvas = Canvas(self.root, width=w, height=h, background = 'black')
        self.canvas.pack()
        for i in range(num_codes):
            code = MatrixScreen(self.canvas, scrnwidth=w, scrnheight=h)
            code.create_code()
            self.codes.append(code)
        self.run_screen_saver()
        self.root.mainloop()

    
    def run_screen_saver(self):
        for code in self.codes:
            code.move_code()
        self.canvas.after(20, self.run_screen_saver)

    def quit(self, event):
        self.root.destroy()



if __name__ == "__main__":
    ScreenSaver(500)  # generate 500 codes to move randomly
