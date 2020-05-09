from champion_quotes import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkf
import tkinter.messagebox as tkmsg
import page_voicelines as pv
from pygame import mixer
import random
import page_voicelines


class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("1024x700")
        self.resizable(0, 0)
        self.title("League Of Legends Sound Board")

        # Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ChampionsPage, GamePage):
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
        img = PhotoImage(file="materials/leagueoflegends_community.png")
        Label = ttk.Label(self, image=img)
        Label.image = img
        Label.place(x=0, y=0, relwidth=1, relheight=1)

        TButton1 = ttk.Button(self, style='my.TButton', command=lambda: controller.show_frame(ChampionsPage), text='''Champions List''',
                              takefocus=False)
        TButton1.place(relx=0.5, rely=0.35, anchor=CENTER, height=70, width=220, bordermode='ignore')

        TButton1_1 = ttk.Button(self, style='my.TButton', command=lambda: controller.show_frame(GamePage), text='''Guessing Game''', takefocus=False)
        TButton1_1.place(relx=0.5, rely=0.5, anchor=CENTER, height=70, width=220, bordermode='ignore')

        TButton1_2 = ttk.Button(self, style='my.TButton', command=None, text='''Support Us''', takefocus=False)
        TButton1_2.place(relx=0.5, rely=0.65, anchor=CENTER, height=70, width=220, bordermode='ignore')

        exitBtnStyle = ttk.Style()
        exitBtnFont = tkf.Font(family='Helvetica', size=18, weight='bold')
        exitBtnStyle.configure('PS.TButton',  background='#8B0000', foreground='#8B0000', font=exitBtnFont)
        exitButton = ttk.Button(self, style='PS.TButton', command=lambda: app.destroy(), text='''EXIT''', takefocus=False)
        exitButton.place(relx=0.97, rely=0.98, anchor=SE, height=50, width=110, bordermode='ignore')




class GamePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        randomChamp = StringVar()
        randomChampQuote = StringVar()
        img = PhotoImage(file="materials/pic_game_background2.png")
        Label = ttk.Label(self, image=img)
        Label.image = img
        Label.place(x=0, y=0, relwidth=1, relheight=1)
        def resetVoice():
            randomChamp.set(random.choice(list(pv.allquotes.keys())))
            randomChampQuote.set(random.choice(list(pv.allquotes[randomChamp.get()])))
        resetVoice()
        #Lives Remaining
        heartsStr = StringVar()
        heartsStr.set(' ♥ ♥ ♥')
        heartsLabel = ttk.Label(self, textvariable=heartsStr, font=tkf.Font(family='Helvetica', size=36, weight='bold'))
        heartsLabel.place(relx=0.0125, rely=0.01)
        #Score
        score = StringVar()
        score.set('0')
        scoreText = ttk.Label(self, text="Score: ", font=tkf.Font(family='Helvetica', size=36, weight='bold'))
        scoreLabel = ttk.Label(self, textvariable=score, font=tkf.Font(family='Helvetica', size=36, weight='bold'))
        scoreText.place(relx=0.78, rely=0.01)
        scoreLabel.place(relx=0.94, rely=0.01)
        #PlayButton
        def btnRandmoVoiceClick():
            mixer.init()
            mixer.music.load(str(randomChamp.get())+' voices/'+str(randomChampQuote.get()))
            mixer.music.play()

        mediumFont = tkf.Font(family='Helvetica', size=18, weight='bold')
        buttonStyle = ttk.Style()
        buttonStyle.configure('my.TButton', font=mediumFont, background='#000000')
        btnRandomVoice = ttk.Button(self, text=' PLAY\nVOICE', style='my.TButton', takefocus=False, command=btnRandmoVoiceClick) #TODO
        btnRandomVoice.place(relx=0.5, rely=0.4, anchor=CENTER, height=80, width=180)
        #TextEntry
        def clear_text(event):
            guess.set('')
        guess = StringVar()
        guess.set('''Enter Champion You Heard''')
        textEntry = ttk.Entry(self, justify=CENTER, textvariable=guess)
        textEntry.bind('<Button-1>', clear_text)
        textEntry.place(relx=0.5, rely=0.6, anchor=CENTER, height=30, width=180)
        #EnterButton
        def btnEnterClick():
            if randomChamp.get().lower() == str(guess.get()).lower():
                guess.set('')
                x = int(score.get())
                x+=1
                strx = str(x)
                score.set(strx)
                resetVoice()
            else:
                guess.set('')
                testString = str(heartsStr.get())
                testString = testString[:-2]
                print(testString)
                heartsStr.set(testString)
                if str(heartsStr.get()) == '':
                    res = tkmsg.askyesno(title='Game Over', message='You lost the game. Would you like to reset?')
                    if res == True:
                        guess.set('')
                        resetVoice()
                        heartsStr.set(' ♥ ♥ ♥')
                        score.set('0')
                    else:
                        backBtnFunc()
        btnEnter = ttk.Button(self, text='SUBMIT', style='my.TButton', takefocus=False, command=btnEnterClick)
        btnEnter.place(relx=0.5, rely=0.65, anchor=CENTER, height=40, width=180)

        #BackButton
        def backBtnFunc():
            guess.set('')
            resetVoice()
            heartsStr.set(' ♥ ♥ ♥')
            score.set('0')
            controller.show_frame(StartPage)
        backBtnStyle = ttk.Style()
        backBtnFont = tkf.Font(family='Helvetica', size=18, weight='bold')
        backBtnStyle.configure('PGG.TButton', background='#cfe8c5', foreground='#788274', font=backBtnFont)
        backButton = ttk.Button(self, style='PGG.TButton', command=backBtnFunc, text='''◄ BACK''',
                                takefocus=False)
        backButton.place(relx=0.03, rely=0.98, anchor=SW, height=50, width=110, bordermode='ignore')
        #exitButton
        exitBtnStyle = ttk.Style()
        exitBtnFont = tkf.Font(family='Helvetica', size=18, weight='bold')
        exitBtnStyle.configure('PS.TButton', background='#8B0000', foreground='#8B0000', font=exitBtnFont)
        exitButton = ttk.Button(self, style='PS.TButton', command=lambda: app.destroy(), text='''EXIT''',
                                takefocus=False)
        exitButton.place(relx=0.97, rely=0.98, anchor=SE, height=50, width=110, bordermode='ignore')



class ChampionsPage(Frame):
    champions = ("Neeko", "Nasus", "Poppy", "Elise")

    @staticmethod
    def play_quote(quote, file):
        mixer.init()
        mixer.music.load(file + quote)
        mixer.music.play()

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def generate_buttons(champion, file):
            for widget in frame.winfo_children():
                widget.destroy()
            quote_name = StringVar()
            z = 1
            x = 0
            for i in champion:
                quote_name.set(i[0:-4])
                ttk.Button(frame, command=lambda y=i: ChampionsPage.play_quote(y, file), text=quote_name.get()) \
                    .place(relx=0.125 * x + 0.0015, rely=0.07 * z - 0.06, height=25, width=120)

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

        frame = LabelFrame(self, text="Selected champion quotes", labelanchor='n')
        frame.place(relx=0.5, rely=0.46, height=600, width=1000, anchor=CENTER)

        champ_select = ttk.Combobox(self, values=ChampionsPage.champions)
        champ_select.place(relx=0.01, rely=0.0065)
        champ_select.bind("<<ComboboxSelected>>", get_btn)

        # BackButton
        backBtnStyle = ttk.Style()
        backBtnFont = tkf.Font(family='Helvetica', size=18, weight='bold')
        backBtnStyle.configure('PGG.TButton', background='#cfe8c5', foreground='#788274', font=backBtnFont)
        backButton = ttk.Button(self, style='PGG.TButton', command=lambda: controller.show_frame(StartPage),
                                text='''◄ BACK''',
                                takefocus=False)
        backButton.place(relx=0.03, rely=0.98, anchor=SW, height=50, width=110, bordermode='ignore')
        # exitButton
        exitBtnStyle = ttk.Style()
        exitBtnFont = tkf.Font(family='Helvetica', size=18, weight='bold')
        exitBtnStyle.configure('PS.TButton', background='#8B0000', foreground='#8B0000', font=exitBtnFont)
        exitButton = ttk.Button(self, style='PS.TButton', command=lambda: app.destroy(), text='''EXIT''',
                                takefocus=False)
        exitButton.place(relx=0.97, rely=0.98, anchor=SE, height=50, width=110, bordermode='ignore')


app = App()
app.mainloop()
