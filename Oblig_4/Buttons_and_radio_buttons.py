import tkinter as tk

class Panel:
    def __init__(self):
        window = tk.Tk() 
        window.title("Moving Ball") 
        
        
        frame = tk.Frame(window, width = 500, height = 250, bg = "gray")
        frame.pack()
        
        bt_something = tk.Button(frame, text = "Left", command = self.handler_something)
       

        bt_something.grid(row = 1, column = 1)
        
        window.mainloop()
       
    def handler_something(self):
        pass

Panel()
