import tkinter as tk
import tkinter.ttk as ttk


import page_start_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    page_start_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    page_start_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x580+652+102")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.313, rely=0.121, relheight=0.69
                , relwidth=0.375)
        self.TLabelframe1.configure(relief='raised')
        self.TLabelframe1.configure(labelanchor="n")
        self.TLabelframe1.configure(relief="raised")
        self.TLabelframe1.configure(cursor="fleur")

        self.TButton1 = ttk.Button(self.TLabelframe1)
        self.TButton1.place(relx=0.167, rely=0.225, height=50, width=200
                , bordermode='ignore')
        self.TButton1.configure(command=page_start_support.toChampionsPage)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Champion List''')
        self.TButton1.configure(cursor="fleur")

        self.TButton1_1 = ttk.Button(self.TLabelframe1)
        self.TButton1_1.place(relx=0.167, rely=0.375, height=50, width=200
                , bordermode='ignore')
        self.TButton1_1.configure(command=page_start_support.toGamePage)
        self.TButton1_1.configure(takefocus="")
        self.TButton1_1.configure(text='''Guessing Game''')
        self.TButton1_1.configure(cursor="fleur")

        self.TButton1_2 = ttk.Button(self.TLabelframe1)
        self.TButton1_2.place(relx=0.167, rely=0.525, height=50, width=200
                , bordermode='ignore')
        self.TButton1_2.configure(command=page_start_support.toSupportLink)
        self.TButton1_2.configure(takefocus="")
        self.TButton1_2.configure(text='''Support Us''')

if __name__ == '__main__':
    vp_start_gui()





