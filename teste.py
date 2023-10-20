from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Entry')
largura = 250
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)


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



janela.mainloop()