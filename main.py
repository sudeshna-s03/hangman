from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import sys


def starts(option):
    if option == 'yes':


        start.destroy()
        
        window = Tk()
        window.attributes("-fullscreen", True)
        window.title("Ready to Hang!! If you didn't find the word less than 4 chances")
        window.geometry("1080x1080")
        chances=5
        image_paths=['5.jpeg','4.jpeg','3.jpeg','2.jpeg','1.jpeg', '0.jpeg']
        img = Image.open(image_paths[chances])
        img = img.resize((200, 200), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        chances=4
        answer_arr=[]



        with open('words.txt') as f:
            words = f.read()

        words = words.split('\n')


        with open('meaning.txt') as f:
            meaning = f.read()

        meaning = meaning.split('\n')


        word_meaning ={}

        for w, m in zip(words, meaning):
            word_meaning.setdefault(w, m)


        answers = random.choice(words)

        answer = answers.upper()


        def clicked(alphabet):
            
            nonlocal chances, answer
            if alphabet in answer:
                if alphabet==answer[0]:
                    btn01["text"] = alphabet
                if alphabet==answer[1]:
                    btn02["text"] = alphabet
                if alphabet==answer[2]:
                    btn03["text"] = alphabet
                if alphabet==answer[3]:
                    btn04["text"] = alphabet
                if alphabet==answer[4]:
                    btn05["text"] = alphabet
                if alphabet==answer[5]:
                        btn06["text"] = alphabet
            else:
                btn29['text'] = chances
                image = Image.open(image_paths[chances])
                image = image.resize((200, 200), Image.ANTIALIAS)
                imgnew = ImageTk.PhotoImage(image)
                panel.configure(image=imgnew)
                panel.image = imgnew
                chances = chances - 1
                if chances<0:
                    k = 'ANSWER: ' + str(answer)
                    messagebox.showinfo("Loose to guess Hanged!!!!!", k)
                    
            if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5]:
                messagebox.showinfo("congratulations", "Win the Game Great Buddy!!!!")
                window.destroy() 
            print(chances)


        def exit():
            sys.exit()

        panel = Label(window, image = img)
        panel.grid(column=0, row=0)



        btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn01.grid(column=5, row=0)
        btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn02.grid(column=6, row=0)
        btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn03.grid(column=7, row=0)
        btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn04.grid(column=8, row=0)
        btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn05.grid(column=9, row=0)
        btn06 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn06.grid(column=10, row=0)




        btn0 = Button(window, text="L",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("L"))
        btn0.grid(column=3, row=5)
        btn1 = Button(window, text="A",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("A"))
        btn1.grid(column=4, row=5)
        btn2 = Button(window, text="O",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("O"))
        btn2.grid(column=5, row=5)
        btn3 = Button(window, text="B",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("B"))
        btn3.grid(column=6, row=5)
        btn4 = Button(window, text="Z",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("Z"))
        btn4.grid(column=7, row=5)
        btn5 = Button(window, text="V",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("V"))
        btn5.grid(column=8, row=5)
        btn6 = Button(window, text="S",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("S"))
        btn6.grid(column=9, row=5)
        btn7 = Button(window, text="C",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("C"))
        btn7.grid(column=10, row=5)
        btn8 = Button(window, text="F",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("F"))
        btn8.grid(column=11, row=5)
        btn9 = Button(window, text="N",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("N"))
        btn9.grid(column=12, row=5)

        btn10 = Button(window, text="P",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("P"))
        btn10.grid(column=4, row=6)
        btn11= Button(window, text="W",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("W"))
        btn11.grid(column=5, row=6)
        btn12 = Button(window, text="G",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("G"))
        btn12.grid(column=6, row=6)
        btn13 = Button(window, text="D",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("D"))
        btn13.grid(column=7, row=6)
        btn14 = Button(window, text="T",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("T"))
        btn14.grid(column=8, row=6)
        btn15 = Button(window, text="Y",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("Y"))
        btn15.grid(column=9, row=6)
        btn16 = Button(window, text="K",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("K"))
        btn16.grid(column=10, row=6)
        btn17 = Button(window, text="M",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("M"))
        btn17.grid(column=11, row=6)

        btn18 = Button(window, text="Q",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("Q"))
        btn18.grid(column=5, row=7)
        btn19= Button(window, text="J",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("J"))
        btn19.grid(column=6, row=7)
        btn20 = Button(window, text="X",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("X"))
        btn20.grid(column=7, row=7)
        btn21 = Button(window, text="H",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("H"))
        btn21.grid(column=8, row=7)
        btn22 = Button(window, text="R",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("R"))
        btn22.grid(column=9, row=7)
        btn23 = Button(window, text="U",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("U"))
        btn23.grid(column=10, row=7)

        btn24 = Button(window, text="I",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("I"))
        btn24.grid(column=7, row=8)
        btn25 = Button(window, text="E",bg="cyan", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda:clicked("E"))
        btn25.grid(column=8, row=8)





        bt1 = Button(window, text="H",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt1.grid(column=17, row=4)
        bt2 = Button(window, text="A",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt2.grid(column=17, row=5)
        bt3 = Button(window, text="N",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt3.grid(column=17, row=6)
        bt4 = Button(window, text="G",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt4.grid(column=17, row=7)
        bt5 = Button(window, text="M",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt5.grid(column=17, row=8)
        bt6 = Button(window, text="A",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt6.grid(column=17, row=9)
        bt7 = Button(window, text="N",bg="Red", fg="Black",width=3,height=1,font=('Helvetica','20'))
        bt7.grid(column=17, row=10)



        bt0 = Button(window, text="EXIT",bg="green", fg="Black",width=6,height=1,font=('Helvetica','17'),command=lambda: exit())
        bt0.grid(column=19, row=11)





        hint = ' HINT :\n\n' + "  "   + str(word_meaning[answers])

        label2=Label(window,text= hint)
        label2.grid(row=7,column=0)


        label1=Label(window,text=" CHANCES YOU HAVE : ")
        label1.grid(row=9,column=0)
        btn29 = Button(window, text="5",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
        btn29.grid(column=1, row=9)

        label3=Label(window,text=" made by: sudeshna")
        label3.grid(row=9,column=22)
        
        window.mainloop()


    else:
        sys.exit()


start = Tk()
start.title("HANGMAN")
start.geometry("500x650")
img = Image.open('hang.jpeg')
img = img.resize((500, 500), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(start, image = img)
panel.grid(column=1, row=0)

btn0 = Button(start, text="START",bg="cyan", fg="Black",width=6,height=1,font=('Helvetica','20'),command=lambda: starts("yes"))
btn0.grid(column=1, row=1)
btn1 = Button(start, text="EXIT",bg="yellow", fg="Black",width=6,height=1,font=('Helvetica','20'),command=lambda: starts("no"))
btn1.grid(column=1, row=2)
start.mainloop()
