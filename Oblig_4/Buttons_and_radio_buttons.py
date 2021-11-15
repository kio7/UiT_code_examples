import tkinter as tk

class Panel:
    def __init__(self):
        window = tk.Tk() 
        window.title("Moving Ball") 
        
        
        frame = tk.Frame(window, width = 500, height = 250, bg = "gray")
        frame.pack()
        
        text_canvas = tk.Canvas()


        bt_left = tk.Button(frame, text = "Left", command = self.handler_left)
        bt_right = tk.Button(frame, text = "Right", command = self.handler_right)

        bt_left.grid(row = 1, column = 1)
        bt_right.grid(row = 1, column = 2)

        window.mainloop()
       
    def handler_left(self):
        pass

    def handler_right(self):
        pass

Panel()
