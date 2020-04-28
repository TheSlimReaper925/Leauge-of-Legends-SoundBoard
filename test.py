from pygame import mixer
from tkinter import *
from tkinter import ttk as t

win = Tk()
win.title("test app")
win.geometry("800x580")
win.resizable(False, False)


# champions = ("Neeko", "other")

neeko_quotes = ("mimic jinx.ogg", "Neeko was out.ogg", "Neeko_063.ogg", "Neeko_Ban.ogg",
                "Neeko_select.ogg", "not being neeko.ogg", "not neeko.ogg")

# champions_selected = (neeko_quotes)

mixer.init()


def play_quote(quote):
    mixer.music.load("neeko voices/"+quote)
    mixer.music.play()


z = 1
x = 0
for i in neeko_quotes:
    t.Button(win, command=lambda y=i: play_quote(y), text=i[0:-4]).grid(row=z, column=x)
    x += 1
    if x == 7:
        x = 0
        z += 1



#
# champ_select = t.Combobox(win, values=champions)
# champ_select.grid(row=0)
# champ_select.bind("<<ComboboxSelected>>", lambda: get_btns(champions_selected[champ_select.current()]))
# btn2 = t.Button(win, command=lambda: play_quote("Neeko_Select.ogg"), text="Neeko select")
# btn2.grid(row=0, column=1)
#
# btn3 = t.Button(win, command=lambda: play_quote("Neeko_063.ogg"), text="Neeko on Nidalee")
# btn3.grid(row=0, column=2)
#
# btn4 = t.Button(win, command=lambda: play_quote("not neeko.ogg"), text="Not Neeko")
# btn4.grid(row=0, column=3)
#
# btn4 = t.Button(win, command=lambda: play_quote("not being neeko.ogg"), text="Not being Neeko")
# btn4.grid(row=0, column=4)

win.mainloop()
