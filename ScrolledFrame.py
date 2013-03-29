from Tkinter import *

class ScrolledFrame(Frame):

        def __init__(self, root, scrollside=RIGHT,**options):

                self.canvas = Canvas(root)
                Frame.__init__(self,self.canvas,options)
                self.vsb = Scrollbar(root, orient='vertical', command=self.canvas.yview)
                self.canvas.configure(yscrollcommand=self.vsb.set)
                self.vsb.pack(side=scrollside,fill='y')
                self.canvas.create_window((4,4),window=self,anchor='nw')
                self.bind('<Configure>', self.OnFrameConfigure)
                

        def OnFrameConfigure(self, event):
                self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        def pack(self, **options):
                self.canvas.pack(**options)
