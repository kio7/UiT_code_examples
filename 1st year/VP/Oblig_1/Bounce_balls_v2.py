import tkinter as tk
from random import randint

def getRandomColor():
    color = "#"
    for _ in range(6):
        color += toHexChar(randint(0, 15))
    return color

def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))
        
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0 
        self.dx = 2
        self.dy = 2
        self.radius = 3
        self.color = getRandomColor()

class BounceBalls:
    def __init__(self):
        self.ballList = []
        
        self.window = tk.Tk()
        self.window.title("Bouncing Balls")
        
        self.window.protocol("WM_DELETE_WINDOW", self.quit) 
        
        self.width = 350
        self.height = 150
        self.canvas = tk.Canvas(self.window, bg = "white", 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = tk.Frame(self.window)
        frame.pack()
        bt_stop = tk.Button(frame, text = "Stop", command = self.stop)
        bt_stop.pack(side = 'left')
        bt_resume = tk.Button(frame, text = "Resume", command = self.resume)
        bt_resume.pack(side= 'left')
        bt_add = tk.Button(frame, text = "+", command = self.add)
        bt_add.pack(side = 'left')
        bt_remove = tk.Button(frame, text = "-", command = self.remove)
        bt_remove.pack(side = 'left')
        bt_faster = tk.Button(frame, text = "Faster", command = self.faster)
        bt_faster.pack(side = 'left')
        bt_slower = tk.Button(frame, text = "Slower", command = self.slower)
        bt_slower.pack(side = 'left')

        self.sleepTime = 100 # Set a sleep time 
        self.isStopped = False
        self.animate()
        
        self.window.mainloop()

    def faster(self):
        self.sleepTime -= 10

    def slower(self):
        self.sleepTime += 10
    
    def stop(self):
        self.isStopped = True
    
    def resume(self):
        self.isStopped = False   
        self.animate()
    
    def add(self):
        self.ballList.append(Ball())
    
    def remove(self): 
        self.ballList.pop()
                                
    def animate(self):
        while not self.isStopped:
            self.canvas.delete("ball") 
            
            for ball in self.ballList:
                self.redisplayBall(ball)

            self.canvas.after(self.sleepTime)
            self.canvas.update()
    
    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
            
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy
    
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, 
            ball.y - ball.radius, ball.x + ball.radius, 
            ball.y + ball.radius, fill = ball.color, tags = "ball")
                              
    def quit(self):
        self.stop()
        self.window.destroy()
               
BounceBalls()
