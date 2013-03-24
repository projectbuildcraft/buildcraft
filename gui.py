"""
    Copyright (C) 2013 Project Buildcraft
    License notice in buildcraft.py
"""
from Tkinter import *
from PIL import Image, ImageTk
import random
import math
import tkFileDialog
import bcorder

class App:

    def __init__(self, master, **options):
        frame = Frame(master,options)
        frame.grid()
        self.master = master

    def get_master(self):
        return self.master

def main_menu():

    root = Tk()
    root.wm_title('Buildcraft - SC2 HOTS Build Order Calculator')
    app = App(root)

    app.my_order = bcorder.Order(filename = "orders/4gate.bo")

    def load(app):
        f = tkFileDialog.askopenfilename()
        app.my_order = bcorder.Order(filename = f)
        analysis_update(app)
        

    app.load = Button(root, text='Load',command=lambda:load(app))
    app.load.grid(row=0,column=0)

    def save(app):
        name = tkFileDialog.asksaveasfilename()
        app.my_order.save(name)

    app.save = Button(root, text='Save',command=lambda:save(app))   
    app.save.grid(row=0,column=1)

    def new(app):
        new_options = new_order()
        if new_options:
            name, race = new_options
            app.my_order = bcorder.Order(name=name, race=race)
            analysis_update(app)

    app.new = Button(root, text='New',command=lambda:new(app))
    app.new.grid(row=0,column=3)    

    def graph(app,f):
        f(app.my_order)

    app.supply = Button(root, text='Supply',command=lambda:graph(app,supply_graph))
    app.supply.grid(row=3,column=0)

    app.army = Button(root, text='Army Value',command=lambda:graph(app,army_value_graph))
    app.army.grid(row=3,column=1)

    app.resource_rate = Button(root, text='Resource Collection Rate',command=lambda:graph(app,resource_collection_rate_graph))
    app.resource_rate.grid(row=3,column=2)

    app.resources = Button(root, text='Resources',command=lambda:graph(app,resource_graph))
    app.resources.grid(row=3,column=3)

    instance_analysis(app.my_order,(app,1,0))

    root.mainloop()

def new_order():
    root = Toplevel()
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
        print text
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

def instance_analysis(order = None, location=None):

    if not location:
        root = Toplevel()

        root.wm_title('Analysis')

        app = App(root)
        row = 0
        column = 0
        app.my_order = order
    else:
        app, row, column = location
        root = app.master

    app.canvas = Canvas(root, width=500,height=500)
    app.canvas.grid(row=row+1,column=column)

    app.minerals = get_image('minerals.gif')
    app.gas = get_image('vespene.gif')
    app.time = get_image('time.gif')
    app.supply = get_image('supply.gif')

    app.canvas.create_image(50,50,image=app.minerals)
    app.canvas.create_image(50,100,image=app.gas)
    app.canvas.create_image(50,150,image=app.supply)

    app.mineral_value = app.canvas.create_text(80,50,anchor=W)
    app.gas_value = app.canvas.create_text(80,100,anchor=W)
    app.supply_value = app.canvas.create_text(80,150,anchor=W)
    
    def refresh(i):
        print app.my_order.name
        
        i = app.my_order.at_time[int(i)-1]

        app.canvas.itemconfig(app.mineral_value,text=str(int(i.minerals)))
        app.canvas.itemconfig(app.gas_value,text=str(int(i.gas)))
        app.canvas.itemconfig(app.supply_value,text=str(int(i.supply))+'/'+str(int(i.cap)))
        
    app.scale = Scale(root, from_=1, to=len(app.my_order.at_time), command=refresh, orient=HORIZONTAL)
    app.scale.grid(row=row,column=column,sticky=E+W)

    root.mainloop()   

def analysis_update(app):
    app.scale.config(to=len(app.my_order.at_time))

def supply_graph(order):
    worker_supply = dict()
    supply = dict()
    cap = dict()

    for i in order.at_time:
        worker_supply[i.time] = i.worker_supply()
        supply[i.time] = i.supply
        cap[i.time] = i.cap

    create_graph([supply,worker_supply,cap],title='Supply',fill=[True,True,False],colors=['red','blue','green'])

def army_value_graph(order):
    minerals = dict()
    total = dict()

    for i in order.at_time:
        minerals[i.time], gas = i.army_value(False)
        total[i.time] = minerals[i.time] + gas

    create_graph([total, minerals],title='Army Value',fill=[True,True],colors=['green','blue'])

def resource_collection_rate_graph(order):
    mineral_rate = dict()
    gas_rate = dict()

    for i in order.at_time:
        mineral_rate[i.time], gas_rate[i.time] = i.resource_rate()

    create_graph([mineral_rate, gas_rate],title='Resource Collection Rate',colors=['blue','green'])

def resource_graph(order):
    minerals = dict()
    gas = dict()

    for i in order.at_time:
        minerals[i.time] = i.minerals
        gas[i.time] = i.gas

    create_graph([minerals,gas],title='Resources on Hand',colors=['blue','green'])

max_ticks = 10

def create_graph(data, fill = None, title = '', colors = None, size = (500,400), padding = (50,30,30,30)):

    ''' Data: Iterable containing dictionaries mapping x values to y values '''

    if fill == None:
        fill = [False]*len(data)
    elif type(fill) == type(True):
        fill = [fill]*len(data)

    if colors == None:
        colors = default_colors[:len(data)]

    width, height = size
    p_top, p_bottom, p_left, p_right = padding

    root = Toplevel()

    root.wm_title(title)
    
    app = App(root)

    app.c = Canvas(root, width = width, height = height)
    app.c.grid()

    app.c.create_rectangle(0,0,width,height,fill='white')
    app.c.create_line(p_left,p_top,p_left,height - p_bottom)
    app.c.create_line(p_left,height - p_bottom,width - p_right,height - p_bottom)
    app.c.create_text(width/2,p_top/2,text = title)

    max_y = max([max(d.values()) for d in data])
    max_x = final_x = max([max(d.keys()) for d in data])
    
    y_ticks = calculate_ticks(float(max_y) / (max_ticks - 1))
    max_y = math.ceil(max_y / y_ticks) * y_ticks
    x_ticks = calculate_ticks(float(max_x) / (max_ticks - 1))
    max_x = math.ceil(max_x / x_ticks) * x_ticks
    x_scale = float(width - p_left - p_right) / max_x
    y_scale = float(height - p_top - p_bottom) / max_y

    def plot_x(x):
        return x * x_scale + p_left

    def plot_y(y):
        return height - p_bottom - y * y_scale

    k = 0
    while k <= max_y:
        i = int(round(k))
        if abs(i - k) < 0.000001 or True:
            y = plot_y(i)
            app.c.create_line(p_left - 3,y,p_left,y)
            app.c.create_text(p_left - 5,y,text = str(i),anchor = E)
        k += y_ticks

    k = 0
    while k <= max_x:
        i = int(round(k))
        if abs(i - k) < 0.000001 or True:
            x = plot_x(i)
            app.c.create_line(x,height - p_bottom + 3,x,height - p_bottom)
            app.c.create_text(x,height - p_bottom + 5,text = str(i),anchor = N)
        k += x_ticks

    for i, d in enumerate(data):
        coords = []
        if fill[i]:
            coords.append((plot_x(0),plot_y(0)))
        coords.append((plot_x(0),plot_y(d[min(d.keys())])))
        for k in d.keys():
            coords.append((plot_x(k),plot_y(d[k])))
        if fill[i]:
            coords.append((plot_x(final_x),plot_y(0)))
            app.c.create_polygon(coords, fill=colors[i])
        else:
            app.c.create_line(coords, fill=colors[i])

    root.mainloop()

def calculate_ticks(v, r = True):
    exponent = math.floor(math.log10(v))
    fraction = v / (10 ** exponent)

    if r:
        if fraction < 1.5:
            nice = 1
        elif fraction < 3:
            nice = 2
        elif fraction < 7:
            nice = 5
        else:
            nice = 10
    else:
        if fraction <= 1:
            nice = 1
        elif fraction <= 2:
            nice = 2
        elif fraction <= 5:
            nice = 5
        else:
            nice = 10

    return nice * 10**exponent

# http://trollop.org/2011/03/15/algorithm-for-optimal-scaling-on-a-chart-axis/


def get_image(src, size = ()):
    image = Image.open('images/'+src)
    if size:
        image = image.resize(size[0],size[1])
    return ImageTk.PhotoImage(image)
