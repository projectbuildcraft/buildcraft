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

def instance_analysis(order):
    root = Tk()

    root.wm_title('Analysis')

    app = App(root)

    app.canvas = Canvas(root, width=500,height=500)
    app.canvas.grid(row=1)

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
        i = order.at_time[int(i)-1]

        app.canvas.itemconfig(app.mineral_value,text=str(int(i.minerals)))
        app.canvas.itemconfig(app.gas_value,text=str(int(i.gas)))
        app.canvas.itemconfig(app.supply_value,text=str(int(i.supply))+'/'+str(int(i.cap)))
        
    app.scale = Scale(root, from_=1, to=len(order.at_time), command=refresh, orient=HORIZONTAL)
    app.scale.grid(row=0,sticky=E+W)

    root.mainloop()

    refresh(app.scale.get())    


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

def create_graph(data = [default_graph()], fill = None, title = '', colors = None, size = (500,400), padding = (50,30,30,30), labels = ('X values','Y values')):

    ''' Data: Iterable containing dictionaries mapping x values to y values '''

    if fill == None:
        fill = [False]*len(data)

    if colors == None:
        colors = default_colors[:len(data)]

    width, height = size
    p_top, p_bottom, p_left, p_right = padding
    x_label, y_label = labels

    root = Tk()

    root.wm_title('Supply over Time')

    app = App(root)

    app.c = Canvas(root, width = width, height = height)
    app.c.grid()


    app.c.create_rectangle(0,0,width,height,fill='white')
    app.c.create_line(p_left,p_top,p_left,height - p_bottom)
    app.c.create_line(p_left,height - p_bottom,width - p_right,height - p_bottom)

    app.c.create_text(width/2,p_top/2,text = title)
    app.c.create_text(width/2,height - p_bottom/2,text = x_label)
#    app.c.create_text(p_left/2,height/2,text = y_label,angle = 90)
    
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

def get_image(src, size = ()):
    image = Image.open('images/'+src)
    if size:
        image = image.resize(size[0],size[1])
    return ImageTk.PhotoImage(image)
