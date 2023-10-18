from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Label')
janela.geometry('250x250')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)
label_nome = Label(janela, width=10, height=2, text='Nome:', font=('Arial 15 bold'), bg=fundo, fg='white')
label_nome.grid(row=0, column=0)
label_idade = Label(janela, width=10, height=2, text='Idade:', font=('Arial 15 bold'), bg=fundo, fg='white')
label_idade.grid(row=1, column=0)
label_pais = Label(janela, width=10, height=2, text='País:', font=('Arial 15 bold'), bg=fundo, fg='white')
label_pais.grid(row=2, column=0)
janela.mainloop()