from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Botão')
largura = 500
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)
botao = Button(janela, width=10, height=2,text="Clica Aqui!", relief='flat', fg='white', bg='black')
botao.place(x=largura//2.5, y=altura//2.5)
janela.mainloop()