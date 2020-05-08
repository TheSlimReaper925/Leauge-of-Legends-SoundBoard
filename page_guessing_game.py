from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkf
import page_voicelines as pv
from pygame import mixer
import random


class GamePage(Frame):




    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        randomChamp = StringVar()
        randomChampQuote = StringVar()
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
        buttonStyle.configure('my.TButton', font=mediumFont)
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
                x = int(score.get())
                x+=1
                strx = str(x)
                score.set(strx)
                resetVoice()
            else:
                testString = str(heartsStr.get())
                testString = testString[:-2]
                print(testString)
                heartsStr.set(testString)
                if str(heartsStr.get()) == '':
                    print("You lose.")
        btnEnter = ttk.Button(self, text='SUBMIT', style='my.TButton', takefocus=False, command=btnEnterClick)
        btnEnter.place(relx=0.5, rely=0.65, anchor=CENTER, height=40, width=180)



