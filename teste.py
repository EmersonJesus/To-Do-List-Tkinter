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
radio.grid(row=0, column=0, padx=10, pady=10)
radio2 = Radiobutton(janela, text='Segundo', value=2)
radio2.grid(row=1, column=0, padx=10, pady=10)
radio3 = Radiobutton(janela, text='Terceiro', value=3)
radio3.grid(row=2, column=0, padx=10, pady=10)
janela.mainloop()