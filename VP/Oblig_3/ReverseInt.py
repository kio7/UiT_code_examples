import tkinter as tk

reverse_num = 0

def reverse_integer(value): 
    global reverse_num

    if(value > 0):
        remainder = value % 10
        reverse_num = (reverse_num * 10) + remainder
        reverse_integer(value // 10)
    
    return reverse_num


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Reverse Integer")
        self.window.geometry("500x130")

        self.num = tk.IntVar()
        tk.Entry(self.window, textvariable = self.num, justify = 'left', width = 60).grid(column = 0, row = 0)        
        self.text = tk.Text(self.window, width = 30)
        self.text.grid(column = 0, row = 1)
        button = tk.Button(self.window, text = 'Reverse', command = self.calculate)
        button.grid(column = 1, row = 0)

        self.window.mainloop()

    def calculate(self):
        user_input = self.num.get()
        result = reverse_integer(user_input)
        self.text.insert('end', f"{result}\n")
        global reverse_num
        reverse_num = 0
        

if __name__ == "__main__":
    GUI()
