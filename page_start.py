import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    img = Image.open("materials/pic_page_start_background.jpg")
    photo = ImageTk.PhotoImage(img)
    top = Toplevel1 (photo, root)
    root.mainloop()

class Toplevel1:

    def __init__(self, photo, top=None):

        self.style = ttk.Style()

        top.geometry("800x580+652+102")
        top.resizable(0, 0)
        top.title("League Of Legends Sound Board")

        self.Label = ttk.Label(top, image=photo)
        self.Label.place(x=0, y=0, relwidth=1, relheight=1)
        self.TButton1 = ttk.Button(top , command=None)
        self.TButton1.place(relx=0.5, rely=0.3, anchor=tk.CENTER, height=50, width=200, bordermode='ignore')
        self.TButton1.configure(text='''Champion List''')


        self.TButton1_1 = ttk.Button(top)
        self.TButton1_1.place(relx=0.5, rely=0.4, anchor=tk.CENTER, height=50, width=200
                , bordermode='ignore')
        self.TButton1_1.configure(command=None)
        self.TButton1_1.configure(text='''Guessing Game''')


        self.TButton1_2 = ttk.Button(top)
        self.TButton1_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=50, width=200
                , bordermode='ignore')
        self.TButton1_2.configure(command=None)
        self.TButton1_2.configure(takefocus="")
        self.TButton1_2.configure(text='''Support Us''')



if __name__ == '__main__':
    vp_start_gui()



