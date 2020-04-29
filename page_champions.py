import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer

champions = ("Neeko", "other")
neeko_quotes = ("Neeko_Select.ogg", "Neeko_Ban.ogg", "Star Guardian spawn music.ogg", "Neeko was out.ogg",
                    "not being neeko.ogg", "not neeko.ogg", "mimic jinx.ogg", "jungle buff neeko.ogg",
                    "last laugh - neeko.ogg", "Neeko - answers now.ogg", "Neeko - changing bodies.ogg",
                    "Neeko - danger beautiful.ogg", "Neeko - emotions.ogg", "Neeko - everywhere.ogg",
                    "Neeko - oovy cat.ogg", "Neeko - oyster.ogg", "Neeko - sho'ma.ogg", "Neeko - words are tricky.ogg",
                    "neeko first - friends.ogg", "no more room.ogg")

def vp_start_gui():

    global val, w, root
    root = tk.Tk()
    top = Toplevel2 (champions, neeko_quotes, root)
    root.mainloop()


class Toplevel2:

    def play_quote(quote):
        mixer.init()
        mixer.music.load("neeko voices/" + quote)
        mixer.music.play()


    def __init__(self, champions, neeko_quotes, top=None):

        top.title("test app")
        top.geometry("800x580")
        top.resizable(False, False)

        def get_btn(event):
            if self.champ_select.current() == 0:
                z = 1
                x = 0
                for i in neeko_quotes:
                    button = tk.Button(top,  command=lambda y=i: Toplevel2.play_quote(y), text=i[0:-4]).place(relx=0.2*x+0.0065, rely=0.25*z-0.16, height=55, width=150)

                    x += 1
                    if x == 5:
                        x = 0
                        z += 1

        self.champ_select = ttk.Combobox(top, values=champions)
        self.champ_select.place(relx=0.0065, rely=0.0065)
        self.champ_select.bind("<<ComboboxSelected>>", get_btn)
        self.champions = champions
        self.neeko_quotes = neeko_quotes




if __name__ == '__main__':
    vp_start_gui()