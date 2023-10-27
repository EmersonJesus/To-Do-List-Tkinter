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
Label(janela, image=img_dock, bg='#32405b').place(x=20, y=25)

# Caderno -----------------
img_caderno = PhotoImage(file='imagens/task.png')
Label(janela, image=img_caderno, bg='#32405b').place(x=350, y=25)

# Cabeçalho ---------------
cabecalho = Label(janela, text='TODAS AS TAREFAS', font='arial 20 bold', fg='white', bg='#32405b')
cabecalho.place(x=60, y=20)

# Main ---------------------
frame = Frame(janela, width=400, height=50, bg='white')
frame.place(x=0, y=188)

tarefa = StringVar()
tarefa_entrada = Entry(frame, width=18, font='arial 20', bd=0)
tarefa_entrada.place(x=10, y=7)
tarefa_entrada.focus

botao = Button(frame, text='ADD', font='arial 20 bold', width=6, bg='#5a95ff', fg='#fff', bd=0)
botao.place(x=300, y=0)

# Caixa de lista --------------------
frame1 = Frame(janela, bd=3, width=700, height=200, bg='#32405b')
frame1.pack(pady=(160, 0))

caixa_lista = Listbox(frame1, font=('arial', 12), width=40, height=16, bg='#32405b', fg='white', cursor='hand2', selectbackground='#5a95ff')
caixa_lista.pack(side=LEFT, fill=BOTH, padx=2)
barra_rolagem = Scrollbar(frame1)
barra_rolagem.pack(side=RIGTH , fill=BOTH)
caixa_lista.config(yscrollcommand=barra_rolagem.set)
barra_rolagem.config(command=caixa_lista.yview)

janela.mainloop()