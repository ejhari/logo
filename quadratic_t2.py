####          QUADRATIC TYPE 2 FRACTAL          ####

from logo import *

class quadratic_Type2(Turtle):
    def imove(self, l, a, i):
        i -= 1
        if i == 0: return self.move(l, a)
        else:
            if a == -90: return self.a_eq(l/4, i)
            elif a == 90: return self.b_eq(l/4, i)

    def a_eq(self, l, i):
            self.imove(l, -90, i)
            self.imove(l, -90, i)
            self.imove(l,  90, i)
            self.imove(l,  90, i)
            self.imove(l,   0, i)
            self.imove(l, -90, i)
            self.imove(l, -90, i)
            self.imove(l,  90, i)
    
    def b_eq(self, l, i):
            self.imove(l,  90, i)
            self.imove(l, -90, i)
            self.imove(l,  90, i)
            self.imove(l,  90, i)
            self.imove(l,   0, i)
            self.imove(l, -90, i)
            self.imove(l, -90, i)
            self.imove(l,  90, i)

    def plot(self, l, i):
        self.angle, c = 0, 0
        while c < 4:
            self.imove(l/4, -90, i)
            self.imove(l/4,  90, i)
            self.imove(l/4,  90, i)
            self.imove(l/4,   0, i)
            self.imove(l/4, -90, i)
            self.imove(l/4, -90, i)
            self.imove(l/4,  90, i)
            self.imove(l/4,  90, i)
            c += 1  
            
    
t = quadratic_Type2(350, 250, 0, c)
t.plot(400, 3)
