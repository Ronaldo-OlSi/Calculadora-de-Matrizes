
def exibir_matriz(matriz):
    """Exibe uma matriz na saída padrão"""
    for linha in matriz:
        print(linha)

def ler_matriz(arquivo):
    matriz = []
    arquivo = open(arquivo, "r")
    linha = arquivo.readline()
    while linha!= "":
        elementos = linha.split()
        for n in range(len(elementos)):
            elementos[n] = int(elementos[n])
        matriz.append(elementos)
        linha = arquivo.readline()
    arquivo.close()
    return matriz

def conferir_matriz(M):
    conf = []
    nlinhas = len(M)
    ncolunas = len(M[0])

    for i in range(nlinhas):
        for j in range(ncolunas):
            if M[i][j] < 0:
                M[i][j] = 0
    for i in range(nlinhas):
        for j in range(ncolunas):
            if M[i][j] > 255:
                M[i][j] = 255

    return conf


