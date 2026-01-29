from tkinter import *
import time

WIDTH = 1000
HEIGHT = 1000
xv = 13
yv = 2

w = Tk()
c = Canvas(w, width=WIDTH, height=HEIGHT, bg="blue")
c.pack()

# Create a triangle polygon
a = c.create_polygon(250, 100, 200, 300, 300, 300, fill="red")

def get_bounds(coords):
    xs = coords[::2]
    ys = coords[1::2]
    return min(xs), min(ys), max(xs), max(ys)

while True:
    co = c.coords(a)
    min_x, min_y, max_x, max_y = get_bounds(co)

    if max_x >= WIDTH or min_x <= 0:
        xv = -xv
    if max_y >= HEIGHT or min_y <= 0:
        yv = -yv

    c.move(a, xv, yv)
    w.update()
    time.sleep(0.01)