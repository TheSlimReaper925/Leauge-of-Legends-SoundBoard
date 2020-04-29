import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


import page_start_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    img = Image.open("materials/pic_page_start_background.jpg")
    photo = ImageTk.PhotoImage(img)
    top = Toplevel1 (photo, root)
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

    def __init__(self, photo, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        self.style = ttk.Style()
        self.style.theme_use('winnative')

        top.geometry("800x580+652+102")
        top.resizable(0, 0)
        top.title("League Of Legends Sound Board")


        self.Label = ttk.Label(top, image=photo)
        self.Label.place(x=0, y=0, relwidth=1, relheight=1)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.5, rely=0.3, anchor=tk.CENTER, height=50, width=200, bordermode='ignore')
        self.TButton1.configure(command=page_start_support.toChampionsPage)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Champion List''')




        self.TButton1_1 = ttk.Button(top)
        self.TButton1_1.place(relx=0.5, rely=0.4, anchor=tk.CENTER, height=50, width=200
                , bordermode='ignore')
        self.TButton1_1.configure(command=page_start_support.toGamePage)
        self.TButton1_1.configure(takefocus="")
        self.TButton1_1.configure(text='''Guessing Game''')






        self.TButton1_2 = ttk.Button(top)
        self.TButton1_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=50, width=200
                , bordermode='ignore')
        self.TButton1_2.configure(command=page_start_support.toSupportLink)
        self.TButton1_2.configure(takefocus="")
        self.TButton1_2.configure(text='''Support Us''')




if __name__ == '__main__':
    vp_start_gui()
