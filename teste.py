from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Olá Mundo')
janela.geometry('300x250')
janela.config(bg=fundo)
janela.iconphoto(False, PhotoImage(file='icon.png'))
janela.resizable(width=False, height=False)

janela.mainloop()