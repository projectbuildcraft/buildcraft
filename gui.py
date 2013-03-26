"""
    Copyright (C) 2013 Project Buildcraft
    License notice in buildcraft.py
"""
from Tkinter import *
from constants import events
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

class EventWidget(Canvas):

    def __init__(self, app, index):
        print index
        Canvas.__init__(self, app.master, height=20)
        self.event = app.my_order.events[index]
        self.at = app.my_order.at[index]
        start = self.at.time
        current = app.scale.get()
        passed_time = current - start
        total_time = events[self.event[0]].time
        actual_time = max(0,min(passed_time,total_time))
        self.fill = self.create_rectangle(2,2,actual_time*5,20,fill='aquamarine',disabledoutline='')
        self.create_rectangle(2,2,total_time*5,20)
        self.create_text(10,10,text=events[self.event[0]].name,anchor=W)
        self.bind('<Button-1>',self.echo)

    def echo(self,location=None):
        print self.event

    def update(self,current):
        print current
        start = self.at.time
        passed_time = current - start
        total_time = events[self.event[0]].time
        actual_time = max(0,min(passed_time,total_time))
        self.coords(self.fill,2,2,actual_time*5,20)
        

def main_menu():

    root = Tk()
    root.wm_title('Buildcraft - SC2 HOTS Build Order Calculator')
    app = App(root)

    app.my_order = bcorder.Order(filename = "orders/Widow Mine Expand.bo")

    add_menu(app)

    add_graph_buttons(app)

    add_instance_analysis(app)

    add_event_list(app)

    root.mainloop()

def load(app):
    f = tkFileDialog.askopenfilename(defaultextension = '.bo', filetypes = [('All files','.*'),('Build order files','.bo')])
    app.my_order = bcorder.Order(filename = f)
    analysis_update(app)

def save(app):
    name = tkFileDialog.asksaveasfilename(defaultextension = '.bo', filetypes = [('All files','.*'),('Build order files','.bo')])
    app.my_order.save(name)

def new(app):
    new_options = new_order()
    if new_options:
        name, race = new_options
        app.my_order = bcorder.Order(name=name, race=race)
        analysis_update(app)

def graph(app,f):
    f(app.my_order)

def add_menu(app):

    app.menubar = Menu(app.master)
    app.menubar.add_command(label='Load',command=lambda:load(app))
    app.menubar.add_command(label='Save',command=lambda:save(app))
    app.menubar.add_command(label='New',command=lambda:new(app))
    app.master.config(menu=app.menubar)

def add_graph_buttons(app):
    app.bottom_buttons = Frame(app.master)
    app.bottom_buttons.pack(side = BOTTOM)

    app.supply = Button(app.bottom_buttons, text='Supply',command=lambda:graph(app,supply_graph))
    app.supply.grid(row=0,column=0,sticky=E+W)

    app.army = Button(app.bottom_buttons, text='Army Value',command=lambda:graph(app,army_value_graph))
    app.army.grid(row=1,column=0,sticky=E+W)

    app.resource_rate = Button(app.bottom_buttons, text='Resource Collection Rate',command=lambda:graph(app,resource_collection_rate_graph))
    app.resource_rate.grid(row=0,column=1,sticky=E+W)

    app.resources = Button(app.bottom_buttons, text='Resources',command=lambda:graph(app,resource_graph))
    app.resources.grid(row=1,column=1,sticky=E+W)

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

def add_instance_analysis(app):

    app.instance = Frame(app.master)
    app.instance.pack(side = LEFT)

    app.canvas = Canvas(app.instance, width=500,height=500)
    app.canvas.pack(side = BOTTOM)

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

        i = int(i)

        for e in app.events:
            e.update(i)
        
        i = app.my_order.at_time[int(i)-1]

        app.canvas.itemconfig(app.mineral_value,text=str(int(i.minerals)))
        app.canvas.itemconfig(app.gas_value,text=str(int(i.gas)))
        app.canvas.itemconfig(app.supply_value,text=str(int(i.supply))+'/'+str(int(i.cap)))

    app.time_scale = Frame(app.instance)
    app.time_scale.pack(side = TOP)

    app.time_icon = Label(app.time_scale, image = app.time)
    app.time_icon.pack(side = LEFT)
    
    app.scale = Scale(app.time_scale, from_=1,to=len(app.my_order.at_time), command=refresh, orient=HORIZONTAL)
    app.scale.pack(side = LEFT, fill=X, expand = True) 

def add_event_list(app):

    app.event_canvas = Canvas(app.master)
    app.event_frame = Frame(app.event_canvas)
    app.event_scrollbar = Scrollbar(app.master,orient='vertical',command=app.event_canvas.yview)
    app.event_canvas.configure(yscrollcommand = app.event_scrollbar.set)
    app.event_scrollbar.pack(side='left',fill='y')
    app.event_canvas.pack(side='right')

    app.events = []
    for i in range(len(app.my_order.events)):
        event_widget = EventWidget(app,i)
        event_widget.pack()
        app.events.append(event_widget)

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