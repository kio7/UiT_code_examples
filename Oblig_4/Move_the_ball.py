import tkinter as tk
    
class Panel:
    def __init__(self):
        window = tk.Tk() 
        window.title("Moving Ball") 
        
        self.canvas = tk.Canvas(window, width = 500, height = 250, bg = "light gray")
        self.canvas.pack()
        
        frame = tk.Frame(window)
        frame.pack()
        
        bt_left = tk.Button(frame, text = "Left", command = self.handler_left)
        bt_right = tk.Button(frame, text = "Right", command = self.handler_right)
        bt_up = tk.Button(frame, text = "Up", command = self.handler_up)
        bt_down= tk.Button(frame, text = "Down", command = self.handler_down)

        bt_left.grid(row = 1, column = 1)
        bt_right.grid(row = 1, column = 2)
        bt_up.grid(row = 1, column = 3)
        bt_down.grid(row = 1, column = 4)
        
        self.canvas.create_oval(240, 115, 270, 145, fill = "red", tags = "Circle", )
        #self.canvas.create_oval()
        window.mainloop()
       
    def handler_right(self):
        position = self.canvas.coords("Circle")
        if position[2] < 500:
            self.canvas.move("Circle", 10, 0)

    def handler_left(self):
        position = self.canvas.coords("Circle")
        if position[0] > 5:
            self.canvas.move("Circle", -10, 0)
    
    def handler_up(self):
        position = self.canvas.coords("Circle")
        if position[1] > 10:
            self.canvas.move("Circle", 0, -10)

    def handler_down(self):
        position = self.canvas.coords("Circle")
        if position[3] < 240:
            self.canvas.move("Circle", 0, +10)

Panel()
