# Create Class Square Att(L) - 
# Methods( get\Set() - Area() - Circumference())

# Create Class Triangle Att(W - H) - 
# Methods( get\Set()  - Area() - Circumference())

# Create Class Rectangle Att(W - H) - 
# Methods( get\Set() - SetTri(Tri) - Area() - Circumference())

from abc import ABC, abstractmethod

#  Base Class
class Shape(ABC):
    def __init__(self, h, w):
        self.h = h
        self.w = w
    @abstractmethod
    def Area(self):
        pass
    @abstractmethod
    def Circumference():
        pass

# Inheritance
class Square(Shape):
    # Constructor
    def __init__(self,L=0):
        super().__init__(L,L)

    # Getter-Setter Methods
    def getLong(self):
        return self.h
    def setLong(self,L):
        self.h = L
    
    # Override Func
    def Area(self):
        return self.h * self.h
    def Circumference(self):
        return self.h * 4

# Inheritance
class Triangle(Shape):
    # Constructor
    def __init__(self,h=0, w=0):
        super().__init__(h,w)

    # Getter-Setter Methods
    def getHeight(self):
        return self.h
    def setHeight(self,h):
        self.h = h
    def getWidth(self):
        return self.w
    def setWidth(self,w):
        self.w = w

    # Override Func
    def Area(self):
        return 0.5 * self.h * self.w
    def Circumference(self):
        return (self.h + self.w) 
# Inheritance
class Rectangle(Shape):
    # Constructor
    def __init__(self,h=0, w=0):
        super().__init__(h,w)

    # Getter-Setter Methods
    def getHeight(self):
        return self.h
    def setHeight(self,h):
        self.h = h
    def getWidth(self):
        return self.w
    def setWidth(self,w):
        self.w = w

    # Override Func
    def Area(self):
        return self.h * self.w
    def Circumference(self):
        return (self.h + self.w) * 2

    # Association
    def setTri(self,Tri):
        self.h = Tri.getHeight()
        self.w = Tri.getWidth()


sq1 = Square(6)
print(sq1.Area())
tr1 = Triangle(2,4)
print(tr1.Area())
rect1 = Rectangle()
rect1.setTri(tr1)
print(rect1.Area())