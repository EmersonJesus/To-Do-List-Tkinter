from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Entry')
largura = 250
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

def dados():
    res_nome['text'] = nome.get()
    res_idade['text'] = idade.get()
    res_pais['text'] = pais.get()
    
    nome.delete(0, END)
    idade.delete(0, END)
    pais.delete(0, END)

# Nome --------------------------------------------
label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 10'), bg=fundo, fg='white', anchor='w')
label_nome.grid(row=0, column=0)
nome = Entry(janela, width=10, font=('Arial 10'))
nome.grid(row=0, column=1, padx=10, pady=5)

# Idade -------------------------------------------------
label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 10'), bg=fundo, fg='white', anchor='w')
label_idade.grid(row=1, column=0)
idade = Entry(janela, width=10, font=('Arial 10'))
idade.grid(row=1, column=1, padx=10, pady=5)

# Pais -------------------------------------------------
label_pais = Label(janela, width=10, height=2, text='Pais: ', font=('Arial 10'), bg=fundo, fg='white', anchor='w')
label_pais.grid(row=2, column=0)
pais = Entry(janela, width=10, font=('Arial 10'))
pais.grid(row=2, column=1, padx=10, pady=5)

# Botão ---------------------------------------------------
botao = Button(janela, width=10, text='Salvar Dados', command=dados)
botao.grid(row=3, column=1)

# Dados -----------------------------------------------------
res_nome = Label(janela, width=10, height=2, text='', font=('Arial 10'), bg=fundo, fg='white', anchor='w')
res_nome.grid(row=4, column=0)
res_idade = Label(janela, width=10, height=2, text='', font=('Arial 10'), bg=fundo, fg='white', anchor='w')
res_idade.grid(row=5, column=0)
res_pais = Label(janela, width=10, height=2, text='', font=('Arial 10'), bg=fundo, fg='white', anchor='w')
res_pais.grid(row=6, column=0)

janela.mainloop()