import tkinter as tk

class Bitwise:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bitwise operators")
        self.window.geometry("700x125")

        # First line
        tk.Label(self.window, text="First number, range 0 - 255").grid(row=1, column=1)
        self.first_string = tk.StringVar(self.window)
        self.first_string.set("0")
        self.first_entry = tk.Entry(self.window, textvariable = self.first_string, justify = 'left', width = 4)
        self.first_entry.grid(row = 1, column = 2)
        self.first_bit = tk.StringVar(self.window)
        self.first_bit.set("00000000") # Setting default value
        first_label = tk.Label(self.window, textvariable=self.first_bit)
        first_label.grid(row=1, column=3)
        tk.Label(self.window, text="Only this for SHIFTRIGHT(1), SHIFTLEFT(1), OCOMP").grid(row=1, column=4)
        
        # Second line
        tk.Label(self.window, text="Second number, range 0 - 255").grid(row=2, column=1)
        self.second_string = tk.StringVar(self.window)
        self.second_string.set("0")
        self.second_entry = tk.Entry(self.window, textvariable = self.second_string, justify = 'left', width = 4)
        self.second_entry.grid(row = 2, column = 2)
        self.second_bit = tk.StringVar(self.window)
        self.second_bit.set("00000000") # Setting default value
        tk.Label(self.window, textvariable=self.second_bit).grid(row=2, column=3)

        # Third line
        tk.Label(self.window, text="Your answer").grid(row=3, column=1)
        self.third_bit = tk.StringVar(self.window)
        self.user_attempt = tk.Entry(self.window, textvariable=self.third_bit, justify='left', width=8)
        self.user_attempt.grid(row=3, column=3)
        self.option_var = tk.StringVar(self.window)
        self.option_var.set("Select operator")
        tk.OptionMenu(self.window, self.option_var, "AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT").grid(row=3, column=4)
        check_button = tk.Button(self.window, text = "Check", width = 10, command = self.button_click)
        check_button.grid(row = 3, column = 5)

        # Fourth line
        tk.Label(self.window, text="Correct answer").grid(row=4, column=1)
        self.correct_answer = tk.StringVar(self.window)
        self.correct_answer.set("0")
        tk.Label(self.window, textvariable=self.correct_answer).grid(row=4, column=3)


        self.window.bind('<FocusOut>', self.process)
        self.window.mainloop()
    
    def button_click(self):
        first_int = int(self.first_string.get())
        if len(self.second_string.get()) > 0:
            second_int =int(self.second_string.get())
        operator = self.option_var.get()
        match operator:
            case "AND":
                answer = first_int & second_int
            case "OR":
                answer = first_int | second_int
            case "OCOMP":
                answer = ~first_int
            case "XOR":
                answer = first_int ^ second_int
            case "SHIFTLEFT":
                answer = first_int<<1
            case "SHIFTRIGHT":
                answer = first_int>>1

        self.correct_answer.set(f"{answer:>08b}")
        
        # Checking if user was correct
        first_string = self.third_bit.get()
        third_int = int(first_string, 2)
        if answer == third_int:
            self.user_attempt.configure(bg="green")
        else:
            self.user_attempt.configure(bg="red")

        self.window.update_idletasks()

    def process(self, e):
        first_int = int(self.first_string.get())
        self.first_bit.set(f"{first_int:>08b}")

        if len(self.second_string.get()) > 0:
            second_int = int(self.second_string.get())
            self.second_bit.set(f"{second_int:>08b}")
        else:
            self.second_bit.set(f"{0:>08b}")

        self.window.update_idletasks()

if __name__ == '__main__':
    Bitwise()
