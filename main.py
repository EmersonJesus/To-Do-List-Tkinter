import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

lista_tarefas = []

# Icone -------------------
img_icone = PhotoImage(file='imagens/task.png')
root.iconphoto(False, img_icone)

# Barra topo ---------------
img_topo = PhotoImage(file='imagens/dock.png')


root.mainloop()