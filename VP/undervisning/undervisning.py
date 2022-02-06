# Primitives


my_string: str = "whatever"
my_int: int = 100
my_float: float = 12.3999
my_large_float: float = 12.312e10
my_bool: bool = False

# Sets
my_set: set =  {1, "Flask", 1.23, "Flask"}

# Sequenses
my_range: range = range(11, 0, -2)
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, [1,2,3], (1,2), "Alo") #Can't be changed

# Dictionaries
my_dictionary: dict = {1 : "one", 2 : "two", 3 : "three"}

# Changing
my_list.append("Whatever")
my_list.insert(2, "Changed")

# Loops: Find all prime below Range
def find_primes():
    lis_of_primes = []
    for i in range(0, 100):
        if is_prime(i):
            lis_of_primes.append(i)

def is_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

# Classes
from math import sin, cos, pi

class Vector:
    def __init__(self, x = 0, y = 0, polar = False): # if given in polar coordinates, interpret x as length and y as angle
        if polar == True:
            self.__x = x*cos(y)
            self.__y = x*sin(y)
        else:
            self.__x = x
            self.__y = y
        self.__file_name = str(id(self)) + '.txt'
    
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def file_name(self):
        return self.__file_name
    @x.setter
    def x(self, value):
        self.__x = value
    @y.setter
    def y(self, value):
        self.__y = value
    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    def __str__(self):
        return f"Vector: ({self.__x}, {self.__y})"
    
    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)
    
    def __mul__(self, other):
        return self.__x * other.__x + self.__y * other.__y

    def save(self):
        with open(file = self.file_name) as file:
            file.write(f"{self.__x}, {self.__y}")
            # file.write(self)

    def load(self):
        with open(file = self.file_name) as file:
            coord = file.readline()
        x_any_y = coord.split(",")
        self.__x = float(x_any_y[0])
        self.__y = float(x_any_y[1])
            