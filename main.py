import tkinter
from tkinter import *

janela = Tk()
janela.title("To-Do-List")
janela.geometry("400x650+400+100")
janela.resizable(False, False)

lista_tarefas = []

# Icone -------------------
img_icone = PhotoImage(file='imagens/task.png')
janela.iconphoto(False, img_icone)

# Barra topo ---------------
img_topo = PhotoImage(file='imagens/topbar.png')
Label(janela, image=img_topo).pack()

img_dock = PhotoImage(file='imagens/dock.png')
Label(janela, image=img_dock, bg='#32405b').place(x=30, y=25)

# Caderno -----------------
img_caderno = PhotoImage(file='imagens/task.png')
Label(janela, image=img_caderno, bg='#32405b').place(x=30, y=25)

# Cabeçalho ---------------
cabecalho = Label(janela, text='TODAS AS TAREFAS', font='arial 20 bold', fg='white', bg='#32405b')
cabecalho.place(x=90, y=20)

janela.mainloop()