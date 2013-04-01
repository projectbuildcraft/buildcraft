from Tkinter import *
import math

max_ticks = 10

def create_graph(data, fill = None, title = '', colors = None, labels = None, size = (600,400), label_width = 150, padding = (50,50,50,50)):

    ''' Data: Iterable containing dictionaries mapping x values to y values '''

    if fill == None:
        fill = [False]*len(data)
    elif type(fill) == type(True):
        fill = [fill]*len(data)

    if colors == None:
        colors = default_colors[:len(data)]

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
    g.c.create_text(width/2,p_top/2,text = title)

    max_y = max([max(d.values()) for d in data])
    max_x = final_x = max([max(d.keys()) for d in data])
    
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
        k += y_ticks

    k = 0
    while k <= max_x:
        i = int(round(k))
        if abs(i - k) < 0.000001 or True:
            x = plot_x(i)
            g.c.create_line(x,height - p_bottom + 3,x,height - p_bottom)
            g.c.create_text(x,height - p_bottom + 5,text = str(i),anchor = N)
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
            g.c.create_polygon(coords, fill=colors[i])
        else:
            g.c.create_line(coords, fill=colors[i])

    # labels
    if labels:
        g.c.create_rectangle(width - label_width + 10,20,width - 10,height-20)
        y = 50
        for i in xrange(len(labels)):
            if fill[i]:
                g.c.create_rectangle(width - label_width + 20,y-10,width - 20,y+10,fill=colors[i])
            else:
                g.c.create_line(width - label_width + 20,y,width - 20,y,fill=colors[i])
            g.c.create_text(width - label_width/2,y - 20,text=labels[i])
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
