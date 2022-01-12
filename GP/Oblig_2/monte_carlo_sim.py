from random import random
from math import sqrt

def calculation(total):
    inside = 0
    number_of_hits = 0

    #Print or no print? printing takes time...
    useranswer = int(input("If you wish to see all points printed to the Terminal type in 1, if not type on 0: "))

    #Iterate for the number of throws
    for i in range(total):
        x2 = random()**2
        y2 = random()**2

        #Increment if inside unit circle.
        if sqrt(x2 + y2) < 1.0:
            inside += 1
            number_of_hits += 1

        if useranswer == 1:
            printer(x2,y2)

    #Print number of hits
    print(f"The number of hits is: {number_of_hits}")
    
    #PI = 4 * (number of hits / throws)
    pi = 4 * (number_of_hits / total)
    print(f"Pi: {pi}")

def printer(x, y):
        print(x, y)

def main():
    calculation(int(input("Enter a number of throws: ")))

if __name__ == "__main__":
    main()
