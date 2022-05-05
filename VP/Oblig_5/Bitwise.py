import tkinter as tk

class Bitwise:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bitwise operators")
        self.window.geometry("700x125")

        # First line
        tk.Label(self.window, text="First number, range 0 - 255").grid(row=1, column=1)
        self.first_int = tk.IntVar(self.window)
        self.first_entry = tk.Entry(self.window, textvariable = self.first_int, justify = 'left', width = 4)
        self.first_entry.grid(row = 1, column = 2)
        self.first_bit = tk.IntVar(self.window)
        self.first_bit.set(f"{0:08b}")
        tk.Label(self.window, textvariable=self.first_bit, width=8).grid(row=1, column=3)
        tk.Label(self.window, text="Only this for SHIFTRIGHT(1), SHIFTLEFT(1), OCOMP").grid(row=1, column=4)
        
        # Second line
        tk.Label(self.window, text="Second number, range 0 - 255").grid(row=2, column=1)
        self.second_int = tk.IntVar(self.window)
        self.second_entry = tk.Entry(self.window, textvariable = self.second_int, justify = 'left', width = 4)
        self.second_entry.grid(row = 2, column = 2)
        self.second_bit = tk.IntVar(self.window)
        self.second_bit.set(f"{0:08b}")
        tk.Label(self.window, textvariable=self.second_bit, width=8).grid(row=2, column=3)

        # Third line
        tk.Label(self.window, text="Your answer").grid(row=3, column=1)
        self.third_int = tk.StringVar(self.window)
        self.third_int.set("0")
        self.user_attempt = tk.Entry(self.window, textvariable=self.third_int, justify='left', width=8)
        self.user_attempt.grid(row=3, column=3)
        self.option_var = tk.StringVar(self.window)
        self.option_var.set("Select operator")
        lis = ["AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT"]
        tk.OptionMenu(self.window, self.option_var, *lis).grid(row=3, column=4)
        check_button = tk.Button(self.window, text = "Check", width = 10, command = self.button_click)
        check_button.grid(row = 3, column = 5)

        # Fourth line
        tk.Label(self.window, text="Correct answer").grid(row=4, column=1)
        self.correct_answer = tk.IntVar(self.window)
        self.correct_answer.set(f"{0:08b}")
        tk.Label(self.window, textvariable=self.correct_answer, width=8).grid(row=4, column=3)
        self.error_label = tk.StringVar(self.window)
        tk.Label(self.window, textvariable=self.error_label).grid(row=4, column=4)


        self.window.bind('<FocusOut>', self.process)
        self.window.mainloop()
    
    def button_click(self):
        first_int = self.first_int.get()
        second_int = self.second_int.get()
        operator = self.option_var.get()
        match operator:
            case "AND":
                answer = first_int & second_int
            case "OR":
                answer = first_int | second_int
            case "OCOMP":
                answer = ~first_int & 255
            case "XOR":
                answer = first_int ^ second_int
            case "SHIFTLEFT":
                answer = first_int << 1 & 255
            case "SHIFTRIGHT":
                answer = first_int >> 1
        try:
            self.correct_answer.set(f"{answer:08b}")
        except UnboundLocalError as e:
            self.error_label.set(f"Error: {e}")
            self.correct_answer.set(f"{0:08b}")
            self.window.update_idletasks()

        
        # Checking if user was correct
        try:
            third_int = int(self.third_int.get(), 2)
            if answer == third_int:
                self.user_attempt.configure(bg="green")
            else:
                self.user_attempt.configure(bg="red")
            self.error_label.set("") # Resetting error label so we know the error is fixed.

        except ValueError as e:
            self.error_label.set(f"Error: {e}")
            self.user_attempt.configure(bg="yellow")
            self.window.update_idletasks()

        self.window.update_idletasks()

    def process(self, e):
        try:
            first_int = self.first_int.get()
            self.first_bit.set(f"{first_int:08b}")
            second_int = self.second_int.get()
            self.second_bit.set(f"{second_int:08b}")
            self.error_label.set("")
            self.user_attempt.configure(bg="white")
            self.window.update_idletasks()
        
        except tk.TclError as e:
            self.error_label.set(f"Error: {e}")
            self.user_attempt.configure(bg="yellow")
            self.window.update_idletasks()


if __name__ == '__main__':
    Bitwise()
