from Tkinter import *

class ScrolledFrame(Frame):

        def __init__(self, root, scrollside=RIGHT, scroll=Y,**options):

                self.canvas = Canvas(root)
                Frame.__init__(self,self.canvas,options)
                if Y in scroll:
                        self.vsb = Scrollbar(root, orient='vertical', command=self.canvas.yview)
                        self.canvas.configure(yscrollcommand=self.vsb.set)
                        self.vsb.pack(side=scrollside,fill='y')
                if X in scroll:
                        self.hsb = Scrollbar(root, orient='horizontal', command=self.canvas.xview)
                        self.canvas.configure(xscrollcommand=self.hsb.set)
                        self.hsb.pack(side=BOTTOM,fill='x')
                self.canvas.create_window((4,4),window=self,anchor='nw')
                self.bind('<Configure>', self.OnFrameConfigure)
                

        def OnFrameConfigure(self, event):
                self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        def pack(self, **options):
                self.canvas.pack(**options)
