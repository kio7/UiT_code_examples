import tkinter as  tk
from random import randint

class DisplayASelectShape_GUI:
    def __init__(self):
        window = tk.Tk() 
        window.title("Select Shapes") 

        var = tk.StringVar()
        var.set("Pick a shape below")
        combo_box = tk.OptionMenu(window, var, "Rectangle", "Oval", "Arc", "Polygon", "Line", \
        command = self.process_selection).pack(fill = 'both')

        self.canvas = tk.Canvas(window)
        self.canvas.create_rectangle(0, 0, 0, 0, tag = "shape")

        self.canvas.pack()

        window.mainloop() 
       
    def process_selection(self, selected_item):
        self.canvas.delete("shape"); 

        if selected_item == "Rectangle":
            self.canvas.create_rectangle(10, 10 , 370, 260, width = 2, tag = "shape")
        elif selected_item == "Arc":
            self.canvas.create_arc(10, 10, 370, 260, start = 0,  extent = 90, width = 2, fill= 'red', tag = "shape")
        elif selected_item == "Oval":
            self.canvas.create_oval(10, 10, 370, 260, width = 2, fill = 'red', tag = "shape")
        elif selected_item == "Polygon":
            coords = [randint(10, 260), randint(10, 260), randint(10, 260), randint(10, 260), randint(10, 260), randint(10, 260), randint(10, 260), randint(10, 260)]
            self.canvas.create_polygon(coords, tag = "shape")
        elif selected_item == "Line":
            self.canvas.create_line(10, 10, 370, 260, width = 2, tag = "shape")

if __name__ == "__main__":
    DisplayASelectShape_GUI() 
