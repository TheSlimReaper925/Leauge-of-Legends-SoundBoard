from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from test import *

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.geometry("1024x700")
		self.resizable(0, 0)
		self.title("League Of Legends Sound Board")

		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)


		self.frames = {}

		for F in (StartPage, ChampionsPage):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

class StartPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		img = tk.PhotoImage(file="materials/leagueoflegends_community.png")
		Label = ttk.Label(self, image=img)
		Label.image = img
		Label.place(x=0, y=0, relwidth=1, relheight=1)

		TButton1 = ttk.Button(self, command=lambda:controller.show_frame(ChampionsPage), text='''Champions List''', takefocus=False)
		TButton1.place(relx=0.5, rely=0.3, anchor=CENTER, height=50, width=200, bordermode='ignore')


		TButton1_1 = ttk.Button(self, command=None, text='''Guessing Game''', takefocus=False)
		TButton1_1.place(relx=0.5, rely=0.4, anchor=CENTER, height=50, width=200, bordermode='ignore')



		TButton1_2 = ttk.Button(self, command=None, text='''Support Us''', takefocus=False)
		TButton1_2.place(relx=0.5, rely=0.5, anchor=CENTER, height=50, width=200, bordermode='ignore')






app = App()
app.mainloop()