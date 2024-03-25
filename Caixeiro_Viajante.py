import numpy as np

def mochileiro(arquivo, formato='coordenadas'):
    # Lendo o arquivo
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    if formato == 'coordenadas':
        # Construindo a lista de cidades
        cidades = [list(map(int, linha.split())) for linha in linhas]

        # Construindo a matriz de distâncias
        n = len(cidades)
        matriz = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i != j:
                    matriz[i][j] = np.sqrt((cidades[i][1] - cidades[j][1])**2 + (cidades[i][2] - cidades[j][2])**2)
    else:
        # Construindo a matriz de distâncias diretamente do arquivo
        matriz = [list(map(int, linha.split())) for linha in linhas]
        matriz = np.array(matriz)
        n = len(matriz)

    visitado = [False]*n

    # Começando pela cidade 0
    rota_do_tesouro = [0]
    visitado[0] = True

    # Função para encontrar a cidade mais próxima
    def proxima_ilha(c):
        min_dist = np.inf
        min_cidade = -1
        for i in range(n):
            if not visitado[i] and matriz[c][i] < min_dist:
                min_dist = matriz[c][i]
                min_cidade = i
        return min_cidade

    # Construindo o caminho
    for _ in range(n-1):
        proxima_cidade = proxima_ilha(rota_do_tesouro[-1])
        rota_do_tesouro.append(proxima_cidade)
        visitado[proxima_cidade] = True

    # Voltando para a cidade inicial
    rota_do_tesouro.append(0)

    # Calculando a distância total
    distancia_total = sum(matriz[rota_do_tesouro[i-1]][rota_do_tesouro[i]] for i in range(1, n+1))

    return rota_do_tesouro, distancia_total

caminho, distancia = mochileiro('1002_cidade.txt', formato='coordenadas')
#para ler o arquivo 29_cidades coloque 'matriz'
#para ler o arquivo 1002_cidade coloque 'coordenadas'
print('Caminho:', caminho)
print('Distância total:', distancia)
