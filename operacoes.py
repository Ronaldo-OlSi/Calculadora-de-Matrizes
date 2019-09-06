import random


def matriz_nula(nlinhas, ncols):
    M = []
    for i in range(nlinhas):
        linha = [0] * ncols
        M.append(linha)
    return M


def transposta(M):

    nlinhas = len(M)
    ncolunas = len(M[0])
    T = matriz_nula(ncolunas, nlinhas)
    for i in range(nlinhas):
        for j in range(ncolunas):
            T[j][i] = M[i][j]
    return T


def inversa(M):
    pass
    return


def eh_igual(A, B):
    nlinhasA, ncolunasA = len(A), len(A[0])
    nlinhasB, ncolunasB = len(B), len(B[0])
    if (nlinhasA == nlinhasB) and (ncolunasA == ncolunasB):
        # podemos prosseguir?
        for i in range(nlinhasA):
            for j in range(ncolunasA):
                if A[i][j] != B[i][j]:
                    return False
        return True

    return False


def somar(A, B):
    C = []
    # verificar se A e B tem a mesma quantidade de linhas e colunas
    nLinhasA, nLinhasB = len(A), len(B)
    nColA, nColB = len(A[0]), len(B[0])
    if (nLinhasA == nLinhasB) and (nColA == nColB):

        for i in range(nLinhasA):
            linha = [0] * nColA
            C.append(linha)
            for j in range(nColA):
                C[i][j] = A[i][j] + B[i][j]
    else:
        print("Matrizes não tem a mesma ordem")

    return C


    # Inverte o valor da matriz
def oposta(M):
    op = []
    for i in range(len(M)):
        linha = [0] * len(M[0])
        op.append(linha)
        for j in range(len(M[0])):
            op[i][j] = -M[i][j]
    return op


def subtrair(A, B):
    return somar(A, oposta(B))


def matriz_aleatoria(M):
    pass
    return


def conferir_par(M):
    conf_p = []
    nlinhas = len(M)
    ncolunas = len(M[0])
    par = True
    for i in range(nlinhas):
        for j in range(ncolunas):
            if nlinhas % 2 == 0:
                par = True
            else:
                par = False
    if par:
        print('É par')
    else:
        print('É Impar')

    return conf_p


def prenche_par(M):

    nlinhas = len(M)
    ncolunas = len(M[0])
    Z = matriz_nula(ncolunas, nlinhas)
    for i in range(0, nlinhas, 2):
        for j in range(ncolunas):
                Z[j][i] = 2
    return Z

def inverter(MA):
    for i in range(0, 50):
        x = len(MA)  # numero de linhas
        y = len(MA[0])  # numero de colunas
        MB = []

    # cria matriz de tamanha igual

    for i in range(0, len(MA)):
        linha = []
        for j in range(0, len(MA[0])):
            linha.append(j + i)
        MB.append(linha)

    for i in range(0, 50):
        MC = []
    # cria matriz invertendo o numero de linhs ecolunas
    for i in range(0, len(MA[0])):
        linha = []
        for j in range(0, len(MA)):
            linha.append(MA[j][i])
        MC.append(linha)
    for i in range(0, len(MC)):
    # inverte a matriz
     MD = []
    for i in range(0, len(MA[0])):
        linha = []
        for j in range(0, len(MA)):
            linha.append(MA[len(MA) - 1 - j][len(MA[0]) - 1 - i])
        MD.append(linha)

    return MD

