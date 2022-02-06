import tkinter as tk
from math import sqrt

class MovableVertices_GUI:
    def __init__(self):
        window = tk.Tk() 
        window.title("Move_2_balls") 

        self.canvas = tk.Canvas(window, width = 400, height = 300)
        self.ball_1 = self.canvas.create_oval(10, 10, 50, 50, fill = "red", width = 2)
        self.ball_2 = self.canvas.create_oval(200, 130, 240, 170, fill = "blue", width = 2)
        self.line = self.canvas.create_line(30, 30, 220, 150, width = 2, tag = "line")
        self.string = "224.72"
        self.text = self.canvas.create_text(135, 87.5, text = self.string, tag = "text")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.move)
        
        window.mainloop() 
        
    def move(self, e):
        ball_1_coords = self.canvas.coords(self.ball_1)
        ball_2_coords = self.canvas.coords(self.ball_2)
        line_coords = self.canvas.coords("line")
        length_line = sqrt((line_coords[0] - line_coords[2])**2 + (line_coords[1] - line_coords[3])**2)
        length_line = f"{length_line:.2f}"
        mouse_distance_ball_1 = sqrt((line_coords[2] - e.x)**2 + (line_coords[3] - e.y)**2)
        mouse_distance_ball_2 = sqrt((line_coords[0] - e.x)**2 + (line_coords[1] - e.y)**2)
        

        if e.x > ball_1_coords[0] and e.y > ball_1_coords[1] and e.x < ball_1_coords[2] and e.y < ball_1_coords[3] and mouse_distance_ball_1 >= 70:
            move_x = e.x - (ball_1_coords[0] + 20)
            move_y = e.y - (ball_1_coords[1] + 20)
            self.canvas.move(self.ball_1, move_x, move_y)
            self.canvas.delete("line")
            self.canvas.create_line(ball_1_coords[0] + 20, ball_1_coords[1] + 20, ball_2_coords[0] + 20, ball_2_coords[1] + 20, width = 2, tag = "line")
            self.canvas.itemconfig(self.text, text = length_line)
            self.canvas.moveto(self.text, (line_coords[0] + line_coords[2]) / 2 - 10, (line_coords[1] + line_coords[3]) / 2 - 10)

        
        elif e.x > ball_2_coords[0] and e.y > ball_2_coords[1] and e.x < ball_2_coords[2] and e.y < ball_2_coords[3] and mouse_distance_ball_2 >= 70:
            move_x = e.x - (ball_2_coords[0] + 20)
            move_y = e.y - (ball_2_coords[1] + 20)
            self.canvas.move(self.ball_2, move_x, move_y)
            self.canvas.delete("line")
            self.canvas.create_line(ball_1_coords[0] + 20, ball_1_coords[1] + 20, ball_2_coords[0] + 20, ball_2_coords[1] + 20, width = 2, tag = "line")
            self.canvas.itemconfig(self.text, text = length_line)
            self.canvas.moveto(self.text, (line_coords[0] + line_coords[2]) / 2 - 10, (line_coords[1] + line_coords[3]) / 2 - 10)


if __name__ == "__main__":
    MovableVertices_GUI() 
