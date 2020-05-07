import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer




class ChampionsPage(tk.Frame):
    champions = ("Neeko", "other")
    neeko_quotes = ("Neeko_Select.ogg", "Neeko_Ban.ogg", "Star Guardian spawn music.ogg", "Neeko was out.ogg",
                    "not being neeko.ogg", "not neeko.ogg", "mimic jinx.ogg", "jungle buff neeko.ogg",
                    "last laugh - neeko.ogg", "Neeko - answers now.ogg", "Neeko - changing bodies.ogg",
                    "Neeko - danger beautiful.ogg", "Neeko - emotions.ogg", "Neeko - everywhere.ogg",
                    "Neeko - oovy cat.ogg", "Neeko - oyster.ogg", "Neeko - sho'ma.ogg", "Neeko - words are tricky.ogg",
                    "neeko first - friends.ogg", "no more room.ogg", "fourth tale.ogg", "home is all around.gg",
                    "magic connects people.ogg", "Neeko will grow.ogg", "slow down, no.ogg", "survival means.ogg")

    @staticmethod
    def play_quote(quote):
        mixer.init()
        mixer.music.load("neeko voices/" + quote)
        mixer.music.play()

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        def get_btn(event):
            quote_name = tk.StringVar()
            if champ_select.current() == 0:
                z = 1
                x = 0
                for i in ChampionsPage.neeko_quotes:
                    quote_name.set(i[0:-4])
                    button = tk.Button(frame, command=lambda y=i: ChampionsPage.play_quote(y), text=quote_name.get()) \
                        .place(relx=0.165 * x + 0.0006, rely=0.08 * z - 0.08, height=45, width=150)

                    x += 1
                    if x == 6:
                        x = 0
                        z += 1


        frame = tk.LabelFrame(self, text="Selected champion quotes", labelanchor='n')
        frame.pack(fill="both", expand=1, padx=10, pady=30)
        champ_select = ttk.Combobox(self, values=ChampionsPage.champions)
        champ_select.place(relx=0.0065, rely=0.0065)
        champ_select.bind("<<ComboboxSelected>>", get_btn)

