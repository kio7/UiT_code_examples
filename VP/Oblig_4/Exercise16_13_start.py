# Made in collaberation with Anders Karlskås and Jørgen Nordås

import tkinter as tk
from gift_wrapping import get_convex_hull

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

def repaint():
    canvas.delete("point")
    if len(points) > 0:
        #
        #
        H = get_convex_hull(points) # call GiftWrapping getConvexHull
        #
        #
        canvas.create_polygon(H, fill = "gray", tags = "point")
        pass

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point", fill = 'black')
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = 'center')
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = 'right')
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = 'right')
        

window = tk.Tk() # Create a window
window.title("Convex Hull") # Set title

width = 900
height = 750
radius = 2
canvas = tk.Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop
