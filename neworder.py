"""
    Copyright (C) 2013 Project Buildcraft
    License notice in buildcraft.py
"""
from Tkinter import *
from PIL import Image, ImageTk
import random

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        self.master = master

    def get_master(self):
        return self.master

def new_order():
    root = Tk()
    root.wm_title('New Order')
    app = App(root)
    app.w = Label(root, text = "Create a new build order")
    app.w.grid(row = 0, columnspan = 3)

    app.e = Entry(root)
    app.e.grid(row = 1, columnspan = 3,sticky = E+W)

    modes = ("Terran","Protoss","Zerg")

    app.here = True

    def submit(app):
        app.proceed = (app.e.get(), app.v.get())
        app.get_master().destroy()

    def _destroy(event):
        app.here = False

    root.bind("<Destroy>", _destroy)

    app.v = StringVar()
    app.v.set('T')
    app.images = []
    for i in range(3):
        text = modes[i]
        image = Image.open('images/'+text+'.png')
        photo = ImageTk.PhotoImage(image.resize((50,50)))
        app.images.append(photo)
        b = Radiobutton(root, text=text, image=photo, indicatoron=0, variable=app.v, value=text[0])
        b.grid(row = 2,column = i)

    app.b = Button(root, text="Done", command=lambda:submit(app))
    app.b.grid(row = 3, columnspan = 3, sticky = E+W)

    app.proceed = ()

    root.mainloop()

    while app.here:
        pass

    return app.proceed

default_colors = ['red','blue','green','yellow','purple','orange']

def default_graph():
    d = {}
    v = 0
    for k in range(100):
        if random.choice([0,1,1]):
            v += 1
        elif v > 0:
            v -= 1
        d[k] = v
    return d

def create_graph(data = [default_graph()], fill = None, title = '', colors = None, size = (500,400), padding = (50,30,30,30)):

    ''' Data: Iterable containing dictionaries mapping x values to y values '''

    if fill == None:
        fill = [False]*len(data)

    if colors == None:
        colors = default_colors[:len(data)]

    width, height = size
    p_top, p_bottom, p_left, p_right = padding

    root = Tk()

    root.wm_title('Supply over Time')

    app = App(root)

    app.c = Canvas(root, width = width, height = height)
    app.c.grid()


    app.c.create_rectangle(0,0,width,height,fill='white')
    app.c.create_line(p_left,p_top,p_left,height - p_bottom)
    app.c.create_line(p_left,height - p_bottom,width - p_right,height - p_bottom)
    app.c.create_text(width/2,p_top/2,text = title)

    max_y = max([max(d.values()) for d in data])
    max_x = max([max(d.keys()) for d in data])
    x_scale = float(width - p_left - p_right) / max_x
    y_scale = float(height - p_top - p_bottom) / max_y

    def plot_x(x):
        return x * x_scale + p_left

    def plot_y(y):
        return height - p_bottom - y * y_scale

    for i, d in enumerate(data):
        coords = []
        if fill[i]:
            coords.append((plot_x(0),plot_y(0)))
        for k in d.keys():
            coords.append((plot_x(k),plot_y(d[k])))
        if fill[i]:
            coords.append((plot_x(max_x),plot_y(0)))
            app.c.create_polygon(coords, fill=colors[i])
        else:
            app.c.create_line(coords, fill=colors[i])

    root.mainloop()
