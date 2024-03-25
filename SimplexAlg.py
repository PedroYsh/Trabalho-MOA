import numpy as np

def padrao(c, A, b):
    
    num_var_original = len(c)  # Número de variáveis originais
    num_restricoes = len(A)     # Número de restrições

    # Adiciona variáveis de folga para as restrições de igualdade
    A_padrao = np.hstack((A, np.eye(num_restricoes)))
    c_padrao = np.hstack((c, np.zeros(num_restricoes)))

    return c_padrao, A_padrao, b
    #A função retorna a função objetivo transformada c_padrao, a matriz de restrições transformada A_padrao e o vetor de restrições inalterado


def simplex_algorithm(c, A, b):
    
    # Transforma o problema em sua forma padrão
    c_padrao, A_padrao, b = padrao(c, A, b)

    num_var = len(c_padrao)        # Número total de variáveis
    num_restricoes = len(A_padrao)  # Número de restrições após adição das variáveis de folga

    # Inicialização da base
    B = np.arange(num_var - num_restricoes, num_var)  # Índices das variáveis básicas
    N = np.arange(0, num_var - num_restricoes)        # Índices das variáveis não básicas

    it = 0  # Contador de iterações
    while True:
        it += 1

        # Passo 1: Calcular as direções básicas
        B_inv = np.linalg.inv(A_padrao[:, B]) #Calcula a inversa da submatriz de A correspondente as variaveis basicas B
        XB = B_inv.dot(b) # Calcula Xb, a solução básica atual, usando a multiplicação da inversa da submatriz básica com o vetor b

        # Passo 2: Calcular os custos relativos
        lambda_t = c_padrao[B].dot(B_inv) #Calcula os custos relativos das variáveis
        CN = c_padrao[N] - lambda_t.dot(A_padrao[:, N])

        # Passo 3: Teste de otimalidade
        #Verifica se todos os custos relativos são não negativos. 
        #Se sim, a solução atual é ótima, e o algoritmo termina retornando a solução encontrada.
        if np.all(CN >= 0):
            # Solução ótima encontrada
            x_star = np.zeros(num_var)
            x_star[B] = XB
            return x_star, it

        # Passo 4: Determinar variável a entrar na base
        #Se o teste de otimalidade falhar, seleciona a variável não básica com o menor custo relativo para entrar na base

        NK = np.argmin(CN)
        x_NK = B_inv.dot(A_padrao[:, N[NK]])

        # Passo 5: Determinar variável a sair da base

        #Calcula as razões entre os elementos da solução básica atual e os 
        #coeficientes correspondentes da variável que está entrando na base.
        #Seleciona a variável básica que limita a solução, ou seja, a 
        #variável que se torna zero primeiro quando a variável entrante se move na direção permitida

        if np.all(x_NK <= 0):
            # Problema ilimitado
            return None, it

        E = np.inf
        for i, x in enumerate(XB):
            if x_NK[i] > 0:
                ratio = x / x_NK[i]
                if ratio < E:
                    E = ratio
                    l = i

        # Passo 6: Atualização
        #Atualiza a base, substituindo a variável básica selecionada na 
        #etapa anterior pela variável não básica que está entrando na base.            
        B[l] = N[NK]

# Função objetivo e restrições do problema original
c_original = np.array([-3, -5])  # Coeficientes da função objetivo original
A_original = np.array([[3, 2],   # Matriz de restrições original
                       [1, 0],
                       [0, 2]])
b_original = np.array([18, 4, 12])  # Vetor de restrições original

# Execução do algoritmo simplex
x_star, num_iteracoes = simplex_algorithm(c_original, A_original, b_original)

# Saída formatada
variavel_solucao = ", ".join([f"x{i+1} = {x}" for i, x in enumerate(x_star)])
variavel_sobra = []

print("Variáveis solução:", variavel_solucao)
print("Variáveis de sobra:", variavel_sobra)
print("Número de iterações:", num_iteracoes)
