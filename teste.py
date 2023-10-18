from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Label')
largura = 500
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)
label_nome = Label(janela, width=largura, height=2, text='Nome:', font=('Arial 15 bold'), bg=fundo, fg='white')
label_nome.pack()
label_idade = Label(janela, width=largura, height=2, text='Idade:', font=('Arial 15 bold'), bg=fundo, fg='white')
label_idade.pack()
label_pais = Label(janela, width=largura, height=2, text='País:', font=('Arial 15 bold'), bg=fundo, fg='white')
label_pais.pack()
janela.mainloop()