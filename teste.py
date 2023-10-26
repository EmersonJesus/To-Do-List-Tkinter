from tkinter import *
from tkinter.ttk import *

fundo = '#242323'

janela = Tk()
janela.title('RadioButton')
largura = 400
altura = 400
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

frame = Frame(janela, width=200, height=200) 

janela.mainloop()