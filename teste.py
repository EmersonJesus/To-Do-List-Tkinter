from tkinter import *
from tkinter.ttk import *

fundo = '#242323'

janela = Tk()
janela.title('RadioButton')
largura = 250
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

radio = Radiobutton(janela, text='Primeiro', value=1)
radio.grid(row=0, column=0)

janela.mainloop()