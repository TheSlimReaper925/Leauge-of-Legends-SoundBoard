from pygame import mixer
from tkinter import *
from tkinter import ttk as t

win = Tk()
win.title("test app")
win.geometry("800x580")
win.resizable(False, False)

champions = ("Neeko", "other")

neeko_quotes = ("mimic jinx.ogg", "Neeko was out.ogg", "Neeko_063.ogg", "Neeko_Ban.ogg",
                "Neeko_select.ogg", "not being neeko.ogg", "not neeko.ogg")

champions_selected = (neeko_quotes)

mixer.init()


def play_quote(quote):
    mixer.music.load("neeko voices/"+quote)
    mixer.music.play()


def get_btn(event):
    if champ_select.current() == 0:
        z = 1
        x = 0
        for i in neeko_quotes:
            t.Button(win, command=lambda y=i: play_quote(y), text=i[0:-4]).grid(row=z, column=x)
            x += 1
            if x == 7:
                x = 0
                z += 1


champ_select = t.Combobox(win, values=champions)
champ_select.grid(row=0)
champ_select.bind("<<ComboboxSelected>>", get_btn)

win.mainloop()