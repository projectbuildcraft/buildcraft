from Tkinter import *

class ScrolledFrame(Frame):

        def __init__(self, root, scrollside=RIGHT, scrolldir=Y,**options):

                self.canvas = Canvas(root)
                Frame.__init__(self,self.canvas,options)
                if Y in scrolldir:
                        self.vsb = Scrollbar(root, orient='vertical', command=self.canvas.yview)
                        self.canvas.configure(yscrollcommand=self.vsb.set)
                        self.vsb.pack(side=scrollside,fill='y')
                if X in scrolldir:
                        self.hsb = Scrollbar(root, orient='horizontal', command=self.canvas.xview)
                        self.canvas.configure(xscrollcommand=self.hsb.set)
                        self.hsb.pack(side=BOTTOM,fill='x')
                self.canvas.create_window((4,4),window=self,anchor='nw')
                def yscroll(event):
                        if event.keycode > 0:
                                self.scroll(-1)
                        else:
                                self.scroll(1)
                self.canvas.bind_all('<MouseWheel>',yscroll)
                self.bind('<Configure>', self.OnFrameConfigure)
                
        def OnFrameConfigure(self, event):
                self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        def pack(self, **options):
                self.canvas.pack(**options)

        def scroll(self, i):
                self.canvas.yview('scroll',i,'units')

        def get_x_scroll(self):
                return self.hsb

        def get_y_scroll(self):
                return self.vsb
