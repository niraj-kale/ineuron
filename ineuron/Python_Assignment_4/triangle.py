class Triangle:
    def setsides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class TriangleArea(Triangle):  
    def calculateArea(self):
        s =  (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return area


t = TriangleArea()
t.setsides(5,5,5)
print(t.calculateArea())
