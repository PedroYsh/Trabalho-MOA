def pokemon(pesos, utilidades, peso_maximo):
    if len(pesos) != len(utilidades):
        raise ValueError("O número de pesos e utilidades não é o mesmo")

    relacao_utilidade_peso = [(utilidades[i] / pesos[i], pesos[i], utilidades[i]) for i in range(len(pesos))]
    relacao_utilidade_peso.sort(reverse=True)

    peso_total = 0
    itens_selecionados = []

    for relacao, peso, utilidade in relacao_utilidade_peso:
        if peso_total + peso <= peso_maximo:
            itens_selecionados.append((peso, utilidade))
            peso_total += peso

    return itens_selecionados, peso_total


def borsa(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    pesos = []
    utilidades = []

    # Extrai os pesos e utilidades da primeira e segunda linha do arquivo
    for linha in linhas:
        if linha.startswith("peso:"):
            pesos = list(map(int, linha.split()[1:]))
        elif linha.startswith("utilidade:"):
            utilidades = list(map(int, linha.split()[1:]))

    if not pesos or not utilidades:
        raise ValueError("Arquivo de entrada mal formatado")

    # Extrai o valor de n da última linha
    peso_maximo = int(linhas[-1].split()[2])

    itens_selecionados, peso_total = pokemon(pesos, utilidades, peso_maximo)

    return itens_selecionados, peso_total

# Exemplo de uso
try:
    itens_selecionados, peso_total = borsa('data_2.txt')
    print("Pokemons selecionados:", itens_selecionados)
    print("Peso total:", peso_total)
except Exception as e:
    print("Ocorreu um erro:", e)
