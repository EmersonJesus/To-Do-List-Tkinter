from tkinter import *
from tkinter.ttk import *

fundo = '#242323'

janela = Tk()
janela.title('Combobox')
largura = 250
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

combo = Combobox(janela)
combo['values'] = ('Opção A', 'Opção B', 'Opção C')
combo.current(1) # Coloca a opção B como ativa por padrão
combo.place(relx=.5, rely=.96, anchor='center')

janela.mainloop()