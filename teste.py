from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Botão')
largura = 500
altura = 250
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

global contador
contador = 0
def executar():
    global contador
    texto1 = 'Impar: '
    texto2 = 'Par: '
    
    if contador%2==0 :
        resultado = texto2 + str(contador)
        label['text'] = resultado
        label['fg'] = 'green'
    else:
        resultado = texto1 + str(contador)
        label['text'] = resultado
        label['fg'] = 'red'
    contador += 1 

label = Label(janela, width=20, height=2, text='Texto', relief='sunken', fg='white', bg=fundo)
label.grid(row=0, column=0, padx=largura//3, pady=10)

botao = Button(janela, command=executar,width=10, height=2,text="Clica Aqui!", relief='raised', fg='white', bg='black')
botao.place(x=largura//2.5, y=altura//2.5)

janela.mainloop()