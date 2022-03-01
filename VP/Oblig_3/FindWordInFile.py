import os
import tkinter as tk


class FindWordInFile:
    def __init__(self):
        self.folders_num = 0
        self.files_num = 0
        self.occurences = 0
        
        window = tk.Tk()
        window.title("Find word in files")

        self.dir_name = tk.StringVar()
        self.dir_entry = tk.Entry(window, textvariable = self.dir_name, justify = 'left', width = 85)
        self.dir_entry.grid(row = 0, column = 0)
        self.dir_entry.insert(-1, "Directory or filename")

        self.word = tk.StringVar()
        self.word_entry = tk.Entry(window, textvariable = self.word, justify = 'left', width = 15)
        self.word_entry.grid(row = 0, column = 1)
        self.word_entry.insert(-1, "Word")

        search_button = tk.Button(window, text = "Search", width = 10, command = self.button_click)
        search_button.grid(row = 0, column = 2)

        self.text = tk.Text(window, height= 40, width = 150)
        self.text.grid(row = 1, columnspan = 3)

        window.mainloop()

    def button_click(self):
        
        self.text.insert('end', "Search start.\n")
        temp = "-"*30 + "\n"
        self.text.insert('end', temp)

        self.recursive_func(self.dir_name.get(), self.word.get())
        self.print_func()

    def recursive_func(self, path, word):
        try:
            dir_names = os.listdir(path)
            dir_names = [f"{path}\\{i}" for i in dir_names if i[0] != "."]
            for elem in dir_names:
                if os.path.isdir(elem):
                    self.folders_num += 1
                    path = os.path.join(path, elem)
                    self.recursive_func(path, word)
                
                else:
                    self.files_num += 1
                    with open(os.path.join(path, elem), "r") as file:
                        for x in file:
                            if word in x:
                                self.occurences += 1
                                self.text.insert('end', f"{path}    {x.strip()}\n")

                    self.files_num += 1

        except FileNotFoundError:
            self.text.insert('end', f"File not found error")
        

    def print_func(self):
        if self.occurences == 0:
            self.text.insert('end', f"{self.word.get()} does not exist.")
            self.folders_num = 0
            self.files_num = 0
            self.occurences = 0
        else:
            self.text.insert('end', '-'*20 + "\n")
            self.text.insert('end', f"Searched: {self.folders_num} directories and {self.files_num} files, found {self.occurences} occurences of '{self.word.get()}'")

if __name__ == "__main__":
    FindWordInFile()
