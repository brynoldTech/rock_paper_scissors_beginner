""" welcome to my channel ..! """
""" lets create rock , paper, scissors using tkinter modules """
""" lets import packages """
from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Hi, lets play rock paper scissors')
root.config(bg='#333')

""" lets create header """
Label(root, text='Rock Paper Scissors', font='arial 20 bold ').pack()

""" user choice """
user_take = StringVar()
Label(root, text='Choose any one : rock , paper scissors', font='arial 15', bg='#570A57').place(x=50, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='black').place(x=90, y=130)

system_picker = random.randint(1, 3)
if system_picker == 1:
    system_picker = 'rock'
elif system_picker == 2:
    system_picker = 'paper'
else:
    system_picker = 'scissors'

result = StringVar()


def play():
    user_pick = user_take.get()
    if user_pick == system_picker:
        result.set('Tie, you both selected same ..!')
    elif user_pick == 'rock' and system_picker == 'paper':
        result.set('you loose , computer selected paper')
    elif user_pick == 'rock' and system_picker == 'scissors':
        result.set('you win computer selected scissors ')
    elif user_pick == 'paper' and system_picker == 'scissors':
        result.set('you loose, computer selected scissors')
    elif user_pick == 'paper' and system_picker == 'rock':
        result.set('you win, computer selected rock')
    elif user_pick == 'scissors' and system_picker == 'rock':
        result.set('you loose, computer selected rock ')
    elif user_pick == 'scissors' and system_picker == 'paper':
        result.set('you win, computer selected paper')
    else:
        result.set('Invalid : choose any one: rock , paper scissors')


""" lets create function to reset """


def reset():
    result.set("")
    user_take.set("")


""" lest create function to exit """


def exit():
    root.destroy()


Entry(root, font='arial 15 bold', textvariable=result, bg='black', width=40).place(x=20, y=250)

""" lets create required buttons .."""
Button(root, font='arial 15 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)
Button(root, font='arial 15 bold', text='RESET', padx=5, bg='seashell4', command=reset).place(x=70, y=310)
Button(root, font='arial 15 bold', text='EXIT', padx=5, bg='seashell4', command=exit).place(x=230, y=310)

root.mainloop()
