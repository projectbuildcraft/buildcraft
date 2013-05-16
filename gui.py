"""
    Copyright (C) 2013 Project Buildcraft
    License notice in buildcraft.py
"""
from Tkinter import *
from constants import events
from constants import CHRONO_BOOST, LARVA
from PIL import Image, ImageTk
import random
import math
import tkFileDialog
import bcorder
from ToolTip import ToolTip
from ScrolledFrame import ScrolledFrame
from graphs import Graph, DataSet
import time
import platform

class App:

    def __init__(self, master, **options):
        self.frame = Frame(master, **options)
        self.frame.grid()
        self.master = master

    def get_master(self):
        return self.master

class EventWidget(Canvas):

    supply_width = 60
    
    def __init__(self, app, index):
        self.height = 20
        self.app = app
        self.index = index
        self.event = app.my_order.events[index]
        self.at = app.my_order.at[index+1]
        start = self.at.time
        current = app.scale.get()
        passed_time = current - start
        total_time = self.app.my_order.event_length(self.index)
        dull = total_time == float('inf') or math.isnan(total_time)
        actual_time = max(0,min(passed_time,total_time))
        self.cooldown = self.app.my_order.get_warp_cooldown(self.index)
        if app.place_by_time:
            if not dull:
                time_width = EventWidget.supply_width + len(self.app.my_order.at_time)*5
                disp = start*5 - 1
            else:
                time_width = 0
                disp = 0
        else:
            if not dull:
                time_width = max(400,EventWidget.supply_width + max(self.cooldown,total_time)*5)
            else:
                time_width = 400
            disp = 0
        Canvas.__init__(self, app.event_frame, height=self.height, width = time_width)
        if self.cooldown and not dull:
            cooldown_passed = max(0,min(self.cooldown,current - start))
            self.cooldown_rect = self.create_rectangle(EventWidget.supply_width+disp,2,EventWidget.supply_width + self.cooldown*5 + disp,self.height)
            self.cooldown_fill = self.create_rectangle(EventWidget.supply_width+disp,2,EventWidget.supply_width + cooldown_passed*5 + disp,self.height,fill='pink')

        if not dull:
            self.fill = self.create_rectangle(EventWidget.supply_width+disp,2,actual_time*5+EventWidget.supply_width+disp,self.height,fill='aquamarine',disabledoutline='')
        self.create_text(2,2,text=str(self.at.supply)+'/'+str(self.at.cap),anchor=N+W)
        if not dull:
            self.full_time = self.create_rectangle(EventWidget.supply_width+disp,2,total_time*5+EventWidget.supply_width+disp,self.height)
        self.create_text(EventWidget.supply_width + 5 + disp,10,text=events[self.event[0]].name,anchor=W)
        self.bind('<Button-1>',self.clicked)
        self.bind('<ButtonRelease-1>',self.unclicked)
        self.bind('<B1-Motion>',self.drag)
        self.passed_str = str(actual_time)+'/'+str(total_time)
        self.tooltip = ToolTip(self,delay=50)
        self.tooltip.configure(text=self.passed_str+' '+self.app.my_order.get_note(self.index))
        
        self.rMenu = Menu(self, tearoff=0)
        self.rMenu.add_command(label='Insert above',command=self.insert_above)
        self.rMenu.add_command(label='Insert below',command=self.insert_below)
        self.rMenu.add_command(label='Delete',command=self.delete)
        self.rMenu.add_command(label='Edit note',command=self.note)
        if app.my_order.can_trick(index):
            if app.my_order.uses_trick(index):
                label = 'Disable gas trick'
            else:
                label = 'Enable gas trick'
            self.rMenu.add_command(label=label,command=self.toggle_trick)
            
        self.bind('<Button-3>',self.popup)

    def echo(self, event=None):
        print self.index

    def chrono_check(self, chrono_index):
        """ Changes this event to be dashed if able to be Chrono Boosted from chrono_index """
        
        if self.app.my_order.can_chrono(self.index, chrono_index):
            self.itemconfig(self.full_time, dash = (4,4))
        else:
            self.itemconfig(self.full_time, dash = None)

    def clicked(self,click_event):
        """ On click, check if Chrono Boost is active, and if so, Chrono Boost this event """
        if self.app.chrono >= 0 and self.app.my_order.can_chrono(self.index, self.app.chrono):
            self.app.insert_chrono(self.index)
            self.app.chrono = -1
        else:
            self.app.drag = self.index

    def unclicked(self,click_event):
        if self.app.drag >= 0:
            change = (click_event.y + 14) / 27
            self.app.my_order.move(self.index, self.index + change)
            self.app.refresh()
            self.app.drag = -1

    def drag(self,drag_event):
        print drag_event.y, self.index, self.app.drag,
        change = 0
        if self.index == self.app.drag:
            if drag_event.y > 40:
                change = (drag_event.y - 13) / 27
            elif drag_event.y < -14:
                change = (drag_event.y + 14) / 27
        else:
            if drag_event.y > 14 or self.index > self.app.drag + 1:
                    change = self.index - self.app.drag
            elif drag_event.y < 14 or self_index < self.app.drag - 1:
                    change = self.app.drag - self.index
        print change
        if change:
            self.app.my_order.move(self.app.drag, self.app.drag + change)
            #self.index += change
            self.app.drag += change
            self.app.refresh()
            
    def update(self,current):
        """ Updates the time completion of this event given current time """
        
        start = self.at.time
        if self.app.place_by_time:
            disp = start*5 - 1
        else:
            disp = 0
        passed_time = current - start
        total_time = self.app.my_order.event_length(self.index)
        dull = total_time == float('inf') or math.isnan(total_time)
        actual_time = max(0,min(passed_time,total_time))
        if not dull:
            self.coords(self.fill,EventWidget.supply_width+disp,2,actual_time*5+EventWidget.supply_width+disp,self.height)
            if self.cooldown:
                cooldown_passed = max(0,min(self.cooldown,current - start))
                self.coords(self.cooldown_fill,EventWidget.supply_width+disp,2,EventWidget.supply_width + cooldown_passed*5 + disp,self.height)
        self.passed_str = str(actual_time)+'/'+str(total_time)
        self.tooltip.configure(text=self.passed_str+' '+self.app.my_order.get_note(self.index))

    def popup(self, event):
        """ Creates right-click menu """
        self.rMenu.post(event.x_root, event.y_root)

    def insert_above(self):
        """ Insert event option above this event """
        self.app.insert_event_choose(self.index)

    def insert_below(self):
        """ Insert event option below this event """
        self.app.insert_event_choose(self.index+1)

    def delete(self):
        """ Remove this event from the build order """
        self.app.my_order.delete(self.index)
        self.app.refresh()

    def note(self):
        """ Allow user to edit note describing this event in a separate window """
        root = Toplevel()
        comment = App(root)
        comment.label = Label(root, text='Comment: ')
        comment.label.pack(side = LEFT)
        comment.entry = Entry(root)
        comment.entry.insert(0,self.app.my_order.get_note(self.index))
        comment.entry.pack(padx = 3, side = LEFT)

        def submit():
            self.app.my_order.set_note(self.index, comment.entry.get())
            self.tooltip.configure(text=self.passed_str+' '+self.app.my_order.get_note(self.index))
            comment.master.destroy()

        comment.button = Button(root, text='OK',command=submit)
        comment.button.pack(side = LEFT)

        root.mainloop()

    def toggle_trick(self):
        self.app.my_order.toggle_trick(self.index)
        self.app.refresh()


def gain_focus(frame):
    frame.force_focus()

class BuildCraftGUI:

    def __init__(app):

        root = Tk()
        root.wm_title('Buildcraft - SC2 HOTS Build Order Calculator')
        app.frame = Frame(root)
        app.frame.grid()
        app.master = root
        app.my_order = bcorder.Order(name='',race='T')

        app.add_menu()

        #add_graph_buttons(app)

        app.add_instance_analysis()

        app.drag = -1

        app.add_event_list()

        root.mainloop()

    def load(app, r = True):
        f = tkFileDialog.askopenfilename(defaultextension = '.bo', initialdir='orders', filetypes = [('All files','.*'),('Build order files','.bo')])
        if f:
            app.my_order = bcorder.Order(filename = f)
            if r:
                app.refresh()

    def save(app):
        if app.my_order.default_location:
            app.my_order.save('')
        else:
            app.save_as()

    def save_as(app):
        name = tkFileDialog.asksaveasfilename(defaultextension = '.bo', initialdir='orders',filetypes = [('All files','.*'),('Build order files','.bo')], initialfile = app.my_order.name)
        if name:
            app.my_order.save(name)
            return True
        return False

    def graph(app,f):
        f(app)

    def toggle_display(app):
        app.place_by_time = not app.place_by_time
        app.refresh()

    def add_menu(app):
        app.menubar = Menu(app.master)
        
        app.file = Menu(app.menubar, tearoff = 0)
        app.menubar.add_cascade(label='File',menu=app.file)
        app.file.add_command(label='Load',command=app.load)
        app.file.add_command(label='Save',command=app.save)
        app.file.add_command(label='Save as',command=app.save_as)
        app.new = Menu(app.file, tearoff = 0)
        app.file.add_cascade(label='New',menu=app.new)
        app.new.add_command(label='Terran',command=lambda:app.new_order('T'))
        app.new.add_command(label='Protoss',command=lambda:app.new_order('P'))
        app.new.add_command(label='Zerg',command=lambda:app.new_order('Z'))

        app.edit = edit = Menu(app.menubar, tearoff = 0)
        app.menubar.add_cascade(label='Edit',menu=edit)
        edit.add_command(label='Undo',command=app.undo, state = DISABLED)
        edit.add_command(label='Redo',command=app.redo, state = DISABLED)

        app.view = Menu(app.menubar, tearoff = 0)
        app.menubar.add_cascade(label='View',menu = app.view)
        app.view.add_command(label='Toggle Display',command=app.toggle_display)
        
        app.graphs = graphs = Menu(app.menubar, tearoff = 0)
        app.menubar.add_cascade(label='Graphs',menu=graphs)
        graphs.add_command(label='Supply',command=app.supply_graph)
        graphs.add_command(label='Army Value',state=NORMAL if has_army(app.my_order) else DISABLED,command=app.army_value_graph)
        graphs.add_command(label='Resource Collection Rate',command=app.resource_collection_rate_graph)
        graphs.add_command(label='Resources',command=app.resource_graph)
        app.master.config(menu=app.menubar)

        app.frame.bind_all('<Control-z>',app.undo)
        app.frame.bind_all('<Control-Y>',app.undo)
        app.frame.bind_all('<Control-Z>',app.redo)
        app.frame.bind_all('<Control-y>',app.redo)

    def graph_buttons_update(app):
        app.graphs.entryconfig('Army Value',state= NORMAL if has_army(app.my_order) else DISABLED)
        app.edit.entryconfig('Undo',state= NORMAL if app.my_order.can_undo() else DISABLED)
        app.edit.entryconfig('Redo',state= NORMAL if app.my_order.can_redo() else DISABLED)

    def undo(app, event=None):
        if app.my_order.can_undo():
            app.my_order.undo()
            app.refresh()

    def redo(app,event=None):
        if app.my_order.can_redo():
            app.my_order.redo()
            app.refresh()

    def new_order(app, race = None):
        if race:
            app.my_order = bcorder.Order(name='',race=race)
            app.refresh()
        else:
            root = Toplevel()
            root.wm_title('New Order')
            new_order = App(root)
            new_order.frame.bind('<FocusOut>',gain_focus)
            new_order.label = Label(root, text = "Create a new build order")
            new_order.label.grid(row = 0, columnspan = 3)

            new_order.entry = Entry(root)
            new_order.entry.grid(row = 1, columnspan = 3,sticky = E+W)

            modes = ("Terran","Protoss","Zerg")

            def submit(app, new_order):
                app.my_order = bcorder.Order(name=new_order.entry.get(),race = new_order.v.get())
                app.refresh()
                new_order.master.destroy()

            new_order.v = StringVar()
            new_order.v.set('T')
            new_order.images = []
            for i in range(3):
                text = modes[i]
                image = Image.open('images/'+text+'.png')
                photo = ImageTk.PhotoImage(image.resize((50,50)))
                new_order.images.append(photo)
                b = Radiobutton(root, text=text, image=photo, indicatoron=0, variable=new_order.v, value=text[0])
                b.grid(row = 2,column = i)

            new_order.b = Button(root, text="Done", command=lambda:submit(app, new_order))
            new_order.b.grid(row = 3, columnspan = 3, sticky = E+W)

            root.mainloop()

    default_colors = ['red','blue','green','yellow','purple','orange']

    def add_instance_analysis(app):

        app.canvas = Canvas(app.master, width=500,height=125)
        app.canvas.pack(side = BOTTOM, expand = 0, fill=X)

        app.minerals = get_image('minerals.gif')
        app.gas = get_image('vespene.gif')
        app.time = get_image('time.gif')
        app.supply = get_image('supply.gif')
        app.larva = get_image('larva.gif')

        app.canvas.mineral_image = app.canvas.create_image(50,25,image=app.minerals)
        app.canvas.gas_image = app.canvas.create_image(50,50,image=app.gas)
        app.canvas.supply_image = app.canvas.create_image(50,75,image=app.supply)
        app.canvas.larva_image = app.canvas.create_image(50,100,image=app.larva)

        app.canvas.mineral_value = app.canvas.create_text(80,25,anchor=W)
        app.canvas.gas_value = app.canvas.create_text(80,50,anchor=W)
        app.canvas.supply_value = app.canvas.create_text(80,75,anchor=W)
        app.canvas.larva_count = app.canvas.create_text(80,100,anchor=W)

        app.canvas.zerg_only = (app.canvas.larva_image, app.canvas.larva_count)

        
        def refresh(i):

            i = int(i)

            for e in app.events:
                e.update(i)
            
            i = app.my_order.at_time[int(i)-1]

            min_rate, gas_rate = i.resource_rate()
            larva_rate = i.larva_rate()
            app.canvas.itemconfig(app.canvas.mineral_value,text=str(int(i.minerals))+' + '+str(int(min_rate))+'/min')
            app.canvas.itemconfig(app.canvas.gas_value,text=str(int(i.gas))+' + '+str(int(gas_rate))+'/min')
            app.canvas.itemconfig(app.canvas.supply_value,text=str(int(i.supply))+'/'+str(int(i.cap)))
            app.canvas.itemconfig(app.canvas.larva_count,text=str(i.units[LARVA])+' + '+str(int(larva_rate))+'/min')

        app.time_scale = Frame(app.master)
        app.time_scale.pack(side = TOP)

        app.time_icon = Label(app.time_scale, image = app.time)
        app.time_icon.pack(side = LEFT)
        
        app.scale = Scale(app.time_scale, from_=1,to=len(app.my_order.at_time), length=300, command=refresh, orient=HORIZONTAL)
        app.scale.pack(side = LEFT,fill=BOTH,expand=1) 

        app.analysis_update()

    def analysis_update(app):
        app.scale.config(to=len(app.my_order.at_time))
        zerg = NORMAL if app.my_order.race == 'Z' else HIDDEN
        for z in app.canvas.zerg_only:
            app.canvas.itemconfig(z, state = zerg)
            

    def refresh(app):
        app.analysis_update()
        app.graph_buttons_update()
        app.event_update()

    def add_event_list(app):

        app.place_by_time = False
        
        app.event_frame = ScrolledFrame(app.master, scrolldir=X+Y,scrollside = LEFT)
        app.event_frame.pack(side = LEFT, fill = BOTH, expand = 1)

        app.event_update()

    def event_update(app):
        app.insert_event_choose(len(app.my_order.events))

    def chrono_check(app, index):
        app.chrono = index
        for e in app.events:
            e.chrono_check(index)

    def insert_event_choose(app, index):
        for w in app.event_frame.children.values():
            w.destroy()
        
        def command(choice):
            e = 0
            while events[e].name != choice:
                e += 1
            if e == CHRONO_BOOST:
                app.chrono_check(index)
            else:
                app.insert_event(index, e)

        variable = StringVar(app.event_frame)

        available = [events[i].name for i in app.my_order.all_available(index)]

        frame = Frame(app.event_frame)
        menu = OptionMenu(frame,variable,*available,command=command)
        menu.pack(side=LEFT)
        label = Label(frame,text='Select event')
        label.pack(side=LEFT)
        
        title = Label(app.event_frame,text=app.my_order.name)
        title.pack()
        
        app.events = []
        for i in xrange(index):
            event_widget = EventWidget(app,i)
            event_widget.pack(anchor=W)
            app.events.append(event_widget)
        frame.pack(anchor=W)
        for i in xrange(index,len(app.my_order.events)):
            event_widget = EventWidget(app,i)
            event_widget.pack(anchor=W)
            app.events.append(event_widget)
        app.chrono = -1

    def insert_event(app, index, event):
        app.my_order.insert([event,''],index)
        app.refresh()

    def insert_chrono(app, target):
        app.my_order.insert_chrono(target, app.chrono)
        app.chrono = -1
        app.refresh()

    def supply_graph(app):
        if not hasattr(app, 'supply_g'):
            app.supply_g = Graph(app.my_order,supply_data,title='Supply',end_value = app.my_order.at[-1].time)
            app.supply_g.start()
        else:
            app.supply_g.recalculate_data(app.my_order)
            app.supply_g.focus_set()
            
    def army_value_graph(app):
        if not hasattr(app, 'army_value_g'):
            app.army_value_g = Graph(app.my_order,army_data,title = 'Army Value',end_value = app.my_order.at[-1].time,options = ['Include Defense'])
            app.army_value_g.start()
        else:
            app.army_value_g.recalculate_data(app.my_order)
            app.army_value_g.focus_set()
            
    def resource_collection_rate_graph(app):
        side_scale = 50 if app.my_order.race == 'Z' else 0
        if not hasattr(app, 'resource_collection_rate_g'):
            app.resource_collection_rate_g = Graph(app.my_order,resource_collection_rate_data,title = 'Resource Collection Rate',side_scale = side_scale,end_value = app.my_order.at[-1].time)
            app.resource_collection_rate_g.start()
        else:
            app.resource_collection_rate_g.recalculate_data(app.my_order)
            app.resource_collection_rate_g.focus_set()

    def resource_graph(app):
        side_scale = 50 if app.my_order.race == 'Z' else 0
        if not hasattr(app, 'resource_g'):
            app.resource_g = Graph(app.my_order,resource_data,title = 'Resources on Hand',side_scale = side_scale,end_value = app.my_order.at[-1].time)
            app.resource_g.start()
        else:
            app.resource_g.recalculate_data(app.my_order)
            app.resource_g.focus_set()

def supply_data(order, args = []):
    worker_supply = dict()
    army_supply = dict()
    cap = dict()

    for i in order.at_time:
        worker_supply[i.time] = i.worker_supply(True)
        army_supply[i.time] = i.supply - worker_supply[i.time]
        cap[i.time] = i.cap

    return [DataSet(army_supply,True,'red','army'),DataSet(worker_supply,True,'blue','workers'),DataSet(cap,False,'green','capacity')]

def has_army(order):
    for i in order.at_time:
        if sum(i.army_value(False)):
            return True
    return False

def army_data(order, args = [False]):
    minerals = dict()
    gas = dict()

    for i in order.at_time:
        minerals[i.time], gas[i.time] = i.army_value(args[0])
        
    return [DataSet(minerals,True,'blue','minerals'),DataSet(gas,True,'green','gas')]

def resource_collection_rate_data(order, args = []):
    mineral_rate = dict()
    gas_rate = dict()
    zerg = order.race == 'Z'
    if zerg:
        larva_rate = dict()

    for i in order.at_time:
        mineral_rate[i.time], gas_rate[i.time] = i.resource_rate()
        if zerg:
            larva_rate[i.time] = i.larva_rate() * 50

    return [DataSet(mineral_rate,False,'blue','minerals'),DataSet(gas_rate,False,'green','gas')] + ([DataSet(larva_rate,False,'orange','larva')] if zerg else [])
    
def resource_data(order, args = []):
    minerals = dict()
    gas = dict()
    zerg = order.race == 'Z'
    if zerg:
        larva = dict()

    for i in order.at_time:
        minerals[i.time] = i.minerals
        gas[i.time] = i.gas
        if zerg:
            larva[i.time] = i.units[LARVA]*50

    return [DataSet(minerals,False,'blue','minerals'),DataSet(gas,False,'green','gas')] + ([DataSet(larva,False,'orange','larva')] if zerg else [])

system = platform.system()
if system == 'Linux':
    imagedir = '/usr/share/games/buildcraft/images/'
else:
    imagedir = 'images/'

def get_image(src, size = ()):
    image = Image.open(imagedir+src)
    if size:
        image = image.resize(size[0],size[1])
    return ImageTk.PhotoImage(image)

BuildCraftGUI()
