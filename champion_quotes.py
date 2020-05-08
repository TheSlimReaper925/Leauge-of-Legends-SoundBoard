import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer
import page_voicelines


class ChampionsPage(tk.Frame):
    champions = ("Neeko", "Nasus", "Poppy", "Elise")

    @staticmethod
    def play_quote(quote, file):
        mixer.init()
        mixer.music.load(file + quote)
        mixer.music.play()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def generate_buttons(champion, file):
            for widget in frame.winfo_children():
                widget.destroy()
            quote_name = tk.StringVar()
            z = 1
            x = 0
            for i in champion:
                quote_name.set(i[0:-4])
                ttk.Button(frame, command=lambda y=i: ChampionsPage.play_quote(y, file), text=quote_name.get()) \
                    .place(relx=0.125 * x + 0.0015, rely=0.1 * z - 0.1, height=45, width=120)

                x += 1
                if x == 8:
                    x = 0
                    z += 1

        def get_btn(event):
            if champ_select.current() == 0:
                generate_buttons(page_voicelines.neeko_quotes, "neeko voices/")
            if champ_select.current() == 1:
                generate_buttons(page_voicelines.nasus_quotes, "Nasus voices/")
            if champ_select.current() == 2:
                generate_buttons(page_voicelines.poppy_quotes, "Poppy voices/")
            if champ_select.current() == 3:
                generate_buttons(page_voicelines.elise_quotes, "elise voices/")


        frame = tk.LabelFrame(self, text="Selected champion quotes", labelanchor='n')
        frame.pack(fill="both", expand=1, padx=10, pady=30)
        champ_select = ttk.Combobox(self, values=ChampionsPage.champions)
        champ_select.place(relx=0.01, rely=0.0065)
        champ_select.bind("<<ComboboxSelected>>", get_btn)
