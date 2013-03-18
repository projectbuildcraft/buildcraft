from Tkinter import *
from PIL import Image, ImageTk

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

