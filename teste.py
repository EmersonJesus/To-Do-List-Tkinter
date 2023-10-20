from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Entry')
largura = 250
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

nome = Entry(janela, width=10, font=('Arial 10'))
nome.grid(row=0, column=0)

janela.mainloop()