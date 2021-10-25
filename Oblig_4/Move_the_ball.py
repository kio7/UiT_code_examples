from tkinter import * 
    
class Panel:
    def __init__(self):
        window = Tk() 
        window.title("Move a Ball") 
        
        self.canvas = Canvas(window, width = 500, height = 250, 
            bg = "light gray")
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        
        bt_circle = Button(frame, text = "Circle", command = self.display_circle)
        bt_left = Button(frame, text = "Left", command = self.left)
        bt_right = Button(frame, text = "Right", command = self.right)
        bt_up = Button(frame, text = "Up", command = self.up)
        bt_down= Button(frame, text = "Down", command = self.down)

        bt_circle.grid(row = 1, column = 2)
        bt_left.grid(row = 2, column = 1)
        bt_right.grid(row = 2, column = 2)
        bt_up.grid(row = 2, column = 3)
        bt_down.grid(row = 2, column = 4)

        
        window.mainloop()
       
    def display_circle(self):
        self.canvas.create_oval(130, 130, 150, 150, fill = "red", tags = "Circle", )
    
    def right(self):
        position = self.canvas.coords("Circle")
        print(position)
        if position[2] < 500:
            self.canvas.move("Circle", 10, 0)

    def left(self):
        position = self.canvas.coords("Circle")
        print(position)
        if position[0] > 5:
            self.canvas.move("Circle", -10, 0)
    
    def up(self):
        position = self.canvas.coords("Circle")
        if position[1] > 0:
            self.canvas.move("Circle", 0, -10)

    def down(self):
        position = self.canvas.coords("Circle")
        if position[3] < 250:
            self.canvas.move("Circle", 0, +10)

Panel() 
