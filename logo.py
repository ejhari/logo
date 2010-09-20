"""Implementation of LOGO IN Python

The class Turtle defines the methods to easily move around
in a user-defined canvas of arbitrary size. The distance 
to be moved, and the angle of rotation can be selected
according to our wish. 
The 'Turtle' is visualized as a triangle which can be 
shown by default,  or hidden, during the movements on the 
canvas. The pen can be 'down', by default, or 'up' too.
All the names used are self-explanatory.
"""   

from math import *
from Tkinter import *
c = Canvas(width = 800, height = 800)
c.pack()

class Turtle():
    def __init__(self, x, y, angle, canvas, pen='down', tv='show'):
        self.x = x
        self.y = y
        self.angle = angle
        self.canvas = canvas
        self.pen = pen
        self.tv = tv 
    
    def move(self, distance, angle):
        self.angle += angle
        x1 = distance * cos((self.angle * 3.14) / 180)
        x2 = distance * sin((self.angle * 3.14) / 180)
        if self.pen == 'down':
            i = self.canvas.create_line(self.x, self.y, self.x + x1, self.y + x2)
            print i
        self.x, self.y = self.x + x1, self.y + x2
        print self.x, self.y, self.angle
                        
    def delete(self, i):
        self.canvas.delete(i)  

    def goto(self, x, y):
        self.x, self.y = x, y

    def turtle(self, rotation=0):
        o_x, o_y, o_a = self.x, self.y, self.angle
        self.move(25.98, rotation)
        self.move(30, -150)
        self.move(30, -120)
        self.move(30, -120)
        self.x, self.y, self.angle = o_x, o_y, o_a

    def turtle_move(self, distance, angle):
        self.move(distance, angle)
        if self.tv == 'show': self.turtle() 
       
    def set_pen(self, pen):
        self.pen = pen

    def set_tv(self, tv):
        self.tv = tv


