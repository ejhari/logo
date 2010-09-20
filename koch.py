####          KOCH'S SNOWFLAKE          ####

from logo import *

class koch(Turtle):
    def imove(self, l, a, i):
        i -= 1
        if i == 0: return self.move(l, a)
        else:
            if a == -60: return self.a_eq(l/3, i)
            elif a == 120: return self.b_eq(l/3, i)
    
    def a_eq(self, l, i):
            self.imove(l, -60, i)
            self.imove(l, -60, i)
            self.imove(l, 120, i)
            self.imove(l, -60, i)
    
    def b_eq(self, l, i):
            self.imove(l, 120, i)
            self.imove(l, -60, i)
            self.imove(l, 120, i)
            self.imove(l, -60, i)

    def flake(self, l, i):
        self.angle, c = 0, 0
        while c < 6:
            self.imove(l/3, -60, i)
            self.imove(l/3, 120, i)
            c += 1 

 
t = koch(350, 250, 0, c)
t.flake(300, 5)
