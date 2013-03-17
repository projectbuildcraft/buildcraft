from Tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.master = master

    def get_master(self):
        return self.master

def new_order():
    root = Tk()
    root.wm_title('New Order')
    app = App(root)
    app.w = Label(root, text = "Create a new build order")
    app.w.pack()

    app.e = Entry(root)
    app.e.pack()

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
    for text in modes:
        b = Radiobutton(root, text=text, variable=app.v, value=text[0])
        b.pack()

    app.b = Button(root, text="Done", command=lambda:submit(app))
    app.b.pack()

    app.proceed = ()

    root.mainloop()

    while app.here:
        pass

    return app.proceed
