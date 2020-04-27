import pygame
from tkinter import *
from tkinter import ttk as t

win = Tk()
win.title("test app")
win.geometry("800x580")
win.resizable(False, False)

pygame.mixer.init()


def play_quote(quote):
    pygame.mixer.music.load("neeko voices/"+quote)
    pygame.mixer.music.play()


btn1 = t.Button(win, command=lambda: play_quote("Neeko_Ban.ogg"), text="Neeko Ban")
btn1.grid(row=0, column=0)

btn2 = t.Button(win, command=lambda: play_quote("Neeko_Select.ogg"), text="Neeko select")
btn2.grid(row=0, column=1)

btn3 = t.Button(win, command=lambda: play_quote("Neeko_063.ogg"), text="Neeko on Nidalee")
btn3.grid(row=0, column=2)

btn4 = t.Button(win, command=lambda: play_quote("not neeko.ogg"), text="Not Neeko")
btn4.grid(row=0, column=3)

win.mainloop()
