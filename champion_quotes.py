import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer
import page_voicelines

champions = ("Neeko", "Nasus", "Poppy", "other")

Neeko_voices = page_voicelines.neeko_quotes
Nasus_voices = page_voicelines.Nasus_voices
Poppy_voices = page_voicelines.Poppy_voices


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel2(root)
    root.mainloop()


class Toplevel2:

    @staticmethod
    def play_quote(quote, file):
        mixer.init()
        mixer.music.load(file + quote)
        mixer.music.play()

    def __init__(self, top=None):

        top.title("test app")
        top.geometry("1024x700")
        top.resizable(False, False)

        def generate_buttons(champion, file):
            for widget in self.frame.winfo_children():
                widget.destroy()
            quote_name = tk.StringVar()
            z = 1
            x = 0
            for i in champion:
                quote_name.set(i[0:-4])
                ttk.Button(self.frame, command=lambda y=i: Toplevel2.play_quote(y, file), text=quote_name.get()) \
                    .place(relx=0.125 * x + 0.0006, rely=0.06 * z - 0.06, height=30, width=120)

                x += 1
                if x == 8:
                    x = 0
                    z += 1

        def get_btn(event):
            if self.champ_select.current() == 0:
                generate_buttons(self.neeko_quotes, "neeko voices/")
            if self.champ_select.current() == 1:
                generate_buttons(self.nasus_quotes, "Nasus voices/")
            if self.champ_select.current() == 2:
                generate_buttons(self.poppy_quotes, "Poppy voices/")

        self.champions = champions
        self.neeko_quotes = Neeko_voices
        self.nasus_quotes = Nasus_voices
        self.poppy_quotes = Poppy_voices

        self.frame = tk.LabelFrame(top, text="Selected champion quotes", labelanchor='n')
        self.frame.pack(fill="both", expand=1, padx=10, pady=30)
        self.champ_select = ttk.Combobox(top, values=champions)
        self.champ_select.place(relx=0.0065, rely=0.0065)
        self.champ_select.bind("<<ComboboxSelected>>", get_btn)


if __name__ == '__main__':
    vp_start_gui()
