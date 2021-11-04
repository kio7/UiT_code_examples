import tkinter as tk

class Panel:
    def __init__(self):
        window = tk.Tk() 
        window.title("Temp Conversion") 
        
        frame = tk.Frame(window, width = 300, height = 150, bg = "gray")
        frame.pack()

        tk.Entry()
        
        bt_convert = tk.Button(frame, text = "Convert", command = self.handler_convert)

        bt_convert.grid(row = 1, column = 1)
        
        window.mainloop()
       
    

    def handler_convert(self):
        pass

def main():
    Panel()


if __name__ == "__main__":
    main()
