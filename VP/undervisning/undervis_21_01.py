from math import pi, sqrt
from turtle import circle

class Circle2D:
    def __init__(self, x = 0.0, y = 0.0, radius = 0.0):
        self.__x = x
        self.__y = y
        self.__radius = radius
    
    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
    
    @property
    def radius(self):
        return self.__radius
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @y.setter
    def y(self, value):
        self.__y = value
    
    @radius.setter
    def radius(self, value):
        self.__radius = value

    def get_area(self):
        return pi*self.__radius**2

    def get_perimeter(self):
        return ((self.__radius * 2) * pi)
    
    def contains_point(self, x, y):
        if sqrt((self.__x - x)**2 + (self.__y - y)**2) < self.__radius:
            return True
        
    def contains(self, circle):
        if sqrt((self.__x - circle.__x)**2 + (self.__y - circle.__y)**2) < self.__radius:
            if circle.__radius > (self.__radius - sqrt((self.__x - circle.__x)**2 + (self.__y - circle.__y)**2)):
                   return True
        
    def overlaps(self, circle):
        if sqrt((self.__x - circle.__x)**2 + (self.__y - circle.__y)**2) < ( self.__radius + circle.__radius):
            return True
        
    def __contains__(self, another):
        pass
    
    def __cmp__(self):
        pass

    def __lt__(self):
        pass

    def __le__(self):
        pass
    
    def __eq__(self):
        pass

    def __ne__(self):
        pass

    def __gt__(self):
        pass
    
    def __ge__(self):
        pass
    
if __name__ == "__main__":
    circle_stor = Circle2D(2, 2, 10)
    circle_liten = Circle2D(3, 3, 5)
    
    print(circle_stor.overlaps(circle_liten))
    