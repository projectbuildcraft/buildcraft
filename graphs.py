from Tkinter import *
import math

max_ticks = 10

class DataSet():

    def __init__(self, data, fill=False, color='black', label=''):
        self.data = data
        self.fill = fill
        self.color = color
        self.label = label

def create_graph(dataset, title = '', size = (600,400), side_scale = None, label_width = 150, padding = (50,50,50,50), end_value = 0):

    ''' Data: Iterable containing dictionaries mapping x values to y values '''

    labels = any([d.label for d in dataset])
    
    if not labels:
        label_width = 0

    width, height = size
    p_top, p_bottom, p_left, p_right = padding

    root = Toplevel()

    root.wm_title(title)
    
    g = Frame(root)
    g.grid()

    g.c = Canvas(root, width = width, height = height)
    g.c.grid()

    g.c.create_rectangle(0,0,width,height,fill='white')
    g.c.create_line(p_left,p_top,p_left,height - p_bottom)
    g.c.create_line(p_left,height - p_bottom,width - p_right - label_width,height - p_bottom)
    if side_scale:
        g.c.create_line(width - p_right - label_width,p_top,width - p_right - label_width,height - p_bottom)
    g.c.create_text(width/2,p_top/2,text = title)


    max_y = max([max(d.data.values()) for d in dataset])
    max_x = final_x = max([max(d.data.keys()) for d in dataset])
    
    y_ticks = calculate_ticks(float(max_y) / (max_ticks - 1))
    max_y = math.ceil(max_y / y_ticks) * y_ticks
    x_ticks = calculate_ticks(float(max_x) / (max_ticks - 1))
    max_x = math.ceil(max_x / x_ticks) * x_ticks
    x_scale = float(width - label_width - p_left - p_right) / max_x
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
            g.c.create_line(p_left - 3,y,p_left,y)
            g.c.create_text(p_left - 5,y,text = str(i),anchor = E)
            if side_scale:
                g.c.create_line(width - p_right - label_width,y,width - p_right - label_width + 3, y)
                g.c.create_text(width - p_right - label_width + 5,y,text = str(i/side_scale),anchor = W)
        k += y_ticks

    k = 0
    while k <= max_x:
        i = int(round(k))
        if abs(i - k) < 0.000001 or True:
            x = plot_x(i)
            g.c.create_line(x,height - p_bottom + 3,x,height - p_bottom)
            g.c.create_text(x,height - p_bottom + 5,text = str(i),anchor = N)
        k += x_ticks

    fill_total = dict()

    coordinates = dict()
        
    for d in dataset[::-1]:
        coords = []
        if d.fill:
            coords.append((plot_x(0),plot_y(0)))
        coords.append((plot_x(0),plot_y(d.data[min(d.data.keys())])))
        for k in d.data.keys():
            if d.fill:
                if k not in fill_total.keys():
                    fill_total[k] = 0
                coords.append((plot_x(k),plot_y(d.data[k] + fill_total[k])))
                fill_total[k] += d.data[k]
            else:
                coords.append((plot_x(k),plot_y(d.data[k])))
        if d.fill:
            coords.append((plot_x(final_x),plot_y(0)))
        coordinates[d] = coords

    for d in dataset:
        if d.fill:
            g.c.create_polygon(coordinates[d], fill=d.color)
        else:
            g.c.create_line(coordinates[d], fill=d.color)

    if end_value:
        x = plot_x(end_value)
        g.c.create_line(x,p_top,x,height - p_bottom,fill='gray')

    # labels
    if labels:
        g.c.create_rectangle(width - label_width + 10,20,width - 10,height-20)
        y = 50
        for d in dataset:
            if d.fill:
                g.c.create_rectangle(width - label_width + 20,y-10,width - 20,y+10,fill=d.color)
            else:
                g.c.create_line(width - label_width + 20,y,width - 20,y,fill=d.color)
            g.c.create_text(width - label_width/2,y - 20,text=d.label)
            y += 50
    

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
