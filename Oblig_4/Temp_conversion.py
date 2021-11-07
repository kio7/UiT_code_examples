import tkinter as tk
    
class LoanCalculator:
    def __init__(self):
        window = tk.Tk() 
        window.title("Temp Conversion") 
        
        tk.Label(window, text = "Enter Celsius").grid(row = 1, column = 1, sticky = "W")
        tk.Label(window, text = "Fahrenheit Temprature").grid(row = 2, column = 1, sticky = "W")
        
        self.celsius = tk.StringVar()
        tk.Entry(window, textvariable = self.celsius, justify = 'right').grid(row = 1, column = 2)
        
        self.result = tk.StringVar()
        converted_to_fahrenheit = tk.Label(window, textvariable = self.result)

        bt_temprature_converter = tk.Button(window, text = "Convert", command = self.temprature_converter)
            
        converted_to_fahrenheit.grid(row = 2, column = 2, sticky = "E")
        bt_temprature_converter.grid(row = 3, column = 2, sticky = "E")
        

        window.mainloop() 

    def temprature_converter(self):
        temprature = float(self.celsius.get())
        temprature = (temprature * 1.8) + 32
        self.result.set(f"{temprature:.1f}")

LoanCalculator()  