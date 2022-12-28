from tkinter import *


class Painter:
    def __init__(self, height, width, color):
        self.root = Tk()
        self.canvas = Canvas(self.root, bg=color, height=height, width=width)

    def draw(self, x, y, height, width, color):
        self.canvas.create_rectangle(x, y, height, width, fill=color)

    def show(self):
        self.canvas.pack()
        # canvas.postscript("canvas.ps")
        mainloop()


paint = Painter(int(input('Enter Canvas height: ')), int(input('Enter Canvas width: ')), input('Enter Canvas color: '))

while True:
    x = int(input('Enter x position: '))
    y = int(input('Enter y position: '))
    height = int(input('Enter shape height: '))
    width = int(input('Enter shape width: '))
    color = input('Enter shape color: ')
    paint.draw(x, y, height, width, color)
    choice = int(input('Do you want to continue: '))
    if not choice:
        paint.show()
        break
