from tkinter import *

fundo = '#242323'

janela = Tk()
janela.title('Contador')
largura = 300
altura = 50
janela.geometry(f'{str(largura)}x{str(altura)}')
janela.config(bg=fundo)
janela.resizable(width=False, height=False)

global contador
contador = 0
def mais():
    global contador
    contador += 1 
    label['text'] =  str(contador)

def menos():
    global contador
    contador -= 1
    label['text'] = str(contador)
    

label = Label(janela, width=20, height=1, text=str(contador), relief='sunken', fg='black', bg='white')
label.grid(row=0, column=0)

mais = Button(janela, command=mais,width=2, height=1,text="+", relief='raised', fg='white', bg='black')
mais.grid(row=0, column=1)

menos = Button(janela, command=menos,width=2, height=1,text="-", relief='raised', fg='white', bg='black')
menos.grid(row=0, column=2)

janela.mainloop()