# ============ 1 (tkinter, ttk) ================
# # დავალება: Button widget ორივე მოდულის გამოყენებით (tkinter, ttk); pack() მეთოდი - side, ipadx, padx
#
# import tkinter
# from tkinter import ttk
#
# win = tkinter.Tk()
# win.geometry("300x200")
#
# tkinter.Button(win, text="From tkinter").pack(
#     side="left", padx=30, ipadx=30
# )
#
#
# ttk.Button(win, text="From ttk").pack(
#     side="right"
# )
#
#
# win.mainloop()
#
#














# ============ 2 (pack() მეთოდი)================
# # დავალება: pack() მეთოდში fill და expand  პარამეტრები
#
# import tkinter
# win = tkinter.Tk()
# win.geometry('400x200')
#
#
# tkinter.Label(win, text='Label1', bg='green').pack(
#     side='left', fill="both", expand=1
# )
# tkinter.Label(win, text='Label2', bg='red').pack(side='top', fill="both", expand=1)
# tkinter.Label(win, text='Label3', bg='yellow').pack(side='top', fill="both", expand=1)
#
# win.mainloop()


# ============ 3 (Frame) ================
# # დავალება: Frame და მასში მოთავსებული ელემენტები

# import tkinter
# win = tkinter.Tk()
# win.geometry('400x200')
#
# fr1 = tkinter.Frame(win)
# fr1.pack()
#
#
# tkinter.Label(fr1, text='Label1', bg='green').pack(
#     side='left'
# )
# tkinter.Label(fr1, text='Label2', bg='red').pack(side='top', fill="both", expand=1)
# tkinter.Label(fr1, text='Label3', bg='yellow').pack(side='top', fill="both", expand=1)
#
#
#
# win.mainloop()


# ============ 4 (Labelframe) ================
# # დავალება: Labelframe(ttk-დან, text, labelanchor პარამეტრები), pack(fill, expand), Label-ზე გრიდი
#
# import tkinter
# from tkinter import ttk
# win = tkinter.Tk()
# win.geometry('400x200')
#
# lb_fr = ttk.LabelFrame(win, text="this is a LabelFrame", labelanchor='n')
# lb_fr.pack(fill="both", expand=1, padx=10, pady=10)
#
# tkinter.Label(lb_fr, text='Label1').grid(row=0, column=0)
# tkinter.Label(lb_fr, text='Label2').grid(row=1, column=0)
# tkinter.Label(lb_fr, text='Label3').grid(row=2, column=0)
#
# win.mainloop()



# ============ 5 (Notebooks) ================
# #მაგალითი: ttk.Notebook, ttk.Frame, add(), select(), enable_traversal();
#
# import tkinter
# from tkinter import ttk
# win = tkinter.Tk()
# win.geometry('400x200')
#
# nb = ttk.Notebook(win)
# nb.pack(fill="both", expand=1, padx=10, pady=10)
#
# tab1 = ttk.Frame(nb)
# tab2 = ttk.Frame(nb)
# tab3 = ttk.Frame(nb)
#
# nb.add(tab1, text="first tab", underline=0)
# nb.add(tab2, text="second tab", underline=0)
# nb.add(tab3, text="third tab", underline=0)
#
# nb.select(tab2)
#
# nb.enable_traversal()
#
# win.mainloop()


# ============ 6 (Combobox) ================
# #მაგალითი: ttk.Combobox, values - 2 სახით, textvariable, postcommand, Virtual Event - <<ComboboxSelected>>


import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.geometry('400x200')


def click_c1():
    print(c1.current())


def select_c1(event):
    if c1.current() == 0:
        c2['values'] = ['მარტი', 'აპრილი', 'მაისი']
    if c1.current() == 1:
        c2['values'] = ['ივნისი', 'ივლისი', 'აგვისტო']
    if c1.current() == 2:
        c2['values'] = ['სექტემბერი', 'ოქტომბერი', 'ნოემბერი']
    if c1.current() == 3:
        c2['values'] = ['დეკემბერი', 'იანვარი', 'თებერვალი']


var = tkinter.StringVar()
var.set("აირჩიე სეზონი")

c1 = ttk.Combobox(win, values=('გაზაფხული', 'ზაფხული', 'შემოდგომა', 'ზამთარი'),
                  textvariable=var, state='readonly', postcommand=click_c1
                  )
# print(dict(c1))
c1.grid(row=0, column=0)

c1.bind('<<ComboboxSelected>>', select_c1)

c2 = ttk.Combobox(win)
c2.grid(row=1, column=0, pady=30)

# c1.current(3)
# print(c1.current())





win.mainloop()


# ============ 7 (Checkbutton) ================
# მაგალითი: ttk.Checkbutton, variable, command, invoke()


# import tkinter
# from tkinter import ttk
# win = tkinter.Tk()
# win.geometry('400x200')
#
# fr1 = ttk.LabelFrame(win, text="Programming Languages")
# fr1.pack(fill='both', expand=1, padx=20, pady=20)
#
#
#
#
# win.mainloop()


# ============ 8 (Radiobutton) ================
# მაგალითი: ttk.Checkbutton, variable, command, invoke()

#
# import tkinter
# from tkinter import ttk
# win = tkinter.Tk()
# win.geometry('400x200')
#
# fr1 = ttk.LabelFrame(win, text="Change Color")
# fr1.pack(side='top', fill='x', padx=20, pady=20)
#
#
#
#
# win.mainloop()


