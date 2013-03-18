from Tkinter import *
from PIL import Image, ImageTk

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
    app.images = []
    for text in modes:
        image = Image.open('images/'+text+'.png')
        photo = ImageTk.PhotoImage(image.resize((50,50)))
        app.images.append(photo)
        b = Radiobutton(root, text=text, image=photo, variable=app.v, value=text[0])
        b.pack()

    app.b = Button(root, text="Done", command=lambda:submit(app))
    app.b.pack()

    app.proceed = ()

    root.mainloop()

    while app.here:
        pass

    return app.proceed

