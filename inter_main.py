
import matplotlib.pyplot as plt
from base_matriz import *
from operacoes import *
from tkinter import *

janela = Tk()
janela.geometry("580x380")
janela.title("Calculos de Matrizes")
heading = Label(text = "Calculadora de Matrizes", bg = "grey", fg = "black",
                width = "500", height = "3")
heading.pack()

A = ler_matriz("matriz50x50.txt")
#B = ler_matriz("matriz2.txt")
T = conferir_matriz(A)
T = transposta(A)

def btTransp():

    print("\n")
    print("***** Transposição de Matriz ****\n")
    print("Original")
    exibir_matriz(A)
    print("Original")
    print("\n")
    print("***********")
    print("Resultado Transposto")
    exibir_matriz(T)
    print("Resultado Transposto")

    arquivo = open('Result_transposta.txt', 'w')
    t = str(T)
    arquivo.write(t)
    arquivo.close()

A = ler_matriz("matriz50x50.txt")
P = conferir_matriz(A)
P = oposta(A)

def btOposta():

    print("\n")
    print("***** Inverter Sinal de Matriz ****\n")
    print("Original")
    exibir_matriz(A)
    print("Original")
    print("\n")
    print("***********")
    print("Resultado com Sinal Inverso")
    exibir_matriz(P)
    print("Resultado com Sinal Inverso")

    arquivo = open('Result_Sinal_inverso.txt', 'w')
    t = str(P)
    arquivo.write(t)
    arquivo.close()

def btimpar():
    A = ler_matriz("matriz50x50.txt")
    # B = ler_matriz("matriz2.txt")
    T = conferir_matriz(A)

    print("\n")
    print("***** Matriz é Par? ****\n")
    print("Original")
    exibir_matriz(A)
    print("Original")
    print("\n")
    print("***********")
    print("Resultado")
    exibir_matriz(T)
    T = conferir_par(A)
    print("Resultado")

    arquivo = open('eh_par_transposta.txt', 'w')
    t = str(T)
    arquivo.write(t)
    arquivo.close()

def btPreenche_par():

    A = ler_matriz("matriz50x50.txt")
    T = conferir_matriz(A)
    T = prenche_par(A)

    print("\n")
    print("***** Matriz é Preenche Par ****\n")
    print("Original")
    exibir_matriz(A)
    print("Original")
    print("\n")
    print("***********")
    print("Resultado Preenche Par")
    exibir_matriz(T)
    print("Resultado Preenche Par")

    arquivo = open('Preenche Par.txt', 'w')
    t = str(T)
    arquivo.write(t)
    arquivo.close()



def btInvert_pos():
    A = ler_matriz("matriz50x50.txt")
    T = conferir_matriz(A)
    I = inverter(A)

    print("\n")
    print("***** Inverte posição da Matriz ****\n")
    print("Original")
    exibir_matriz(A)
    print("Original")
    print("\n")
    print("***********")
    print("Resultado Inverte posição da Matriz")
    exibir_matriz(I)
    print("Resultado Inverte posição da Matriz")

    arquivo = open('Inverte_pos.txt', 'w')
    t = str(I)
    arquivo.write(t)
    arquivo.close()


'''
register = Button(janela, text = "Salvar", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 15, y = 320)'''


Conf = Button(janela, text = "Inverter a Ordem", width = "30", height = "2", command = btInvert_pos, bg = "grey")
Conf.place(x = 350, y = 70)

Conf = Button(janela, text = "Conferir Par", width = "30", height = "2", command = btimpar, bg = "grey")
Conf.place(x = 350, y = 120)

sub = Button(janela, text = "Preenche Pos. Pares c/ 2", width = "30", height = "2", command = btInvert_pos, bg = "grey")
sub.place(x = 350, y = 170)

In = Button(janela, text = "Iversão de Valor", width = "30", height = "2", command = btOposta, bg = "grey")
In.place(x = 350, y = 220)

transposta = Button(janela, text = "Transposta", width = "30", height = "2", command = btTransp, bg = "grey")
transposta.place(x = 350, y = 270)

lb = Label(janela, text = "STATUS", bg = "#C0C0C0")
lb.place(x = 435, y = 315)
lb11 = Label(janela, text = "DICA: Use Tab para navegar!", bg = "#C0C0C0")
lb11.place(x = 90, y = 315)

#plt.show()
janela.mainloop()