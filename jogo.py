from random import randint
from constantes import *

def ini_matriz(tamanho):
    """INICIA A MATRIZ"""
    m = [[0 for g in range(tamanho[1])] for i in range(tamanho[0])]
    return m

def imprime_coordenada():
    """FAZ A REPRESENTAÇÃO DA COORDENADA"""
    global colunas
    print('\n', end='')
    for i in range(1, colunas+1):
        if i > 9:
            print(str(i) + ' ', end='')  # Retirei um espaço para que a posição dos numeros não fique errada
        else:
            print(str(i) + '  ', end='')
    print('\n' + '-' * 2 + '-' * ((colunas * 3)-3))  # Um traço que entre os numeros da coluna

def mostra_matriz(tab):
    """PRINTA A MATRIZ """
    imprime_coordenada()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j],  end='  ')
        print()

def jogada(matriz, coluna, jogador):
    """
    COLOCA A JOGADA NA MATRIZ, CONSIDERANDO SEMPRE A ULTIMA LINHA VAZIA EM RELAÇÃO A COLUNA
    :param matriz: Tabuleiro
    :param coluna: Numeração da coluna
    :param jogador: Quais dos jogadores está na vez
    :return: Retorna a jogada no tabuleiro
    """
    for i in range(len(matriz) -1, -1, -1):
        if matriz[i][coluna] == 0:
            jogador, matriz[i][coluna] = matriz[i][coluna], jogador
    return matriz


def inicia_turno():
    """
    Escohe um jogador aleatoriamente para iniciar a partida
    :return: JOG1 ou JOG2 aleatoriamente
    """
    dado = randint(0, 1)
    if dado == 0:
        return JOG1
    else:
        return JOG2

def troca_turno(turno):
    """
    Troca o turno dos jogadores
    :param turno: Um string que representa o jogador atual
    :return: Um string que representa o outro jogador para o qual o turno vai ser trocado
    """
    if turno == JOG1:
        return JOG2
    else:
        return JOG1

def jogada_formato_valido(escolha):
    """
    Verifica se uma jogada tem um formato xy, onde x e y são números
    :param escolha: Um String que representa a jogada
    :return: True se o formato for válido ou False caso contrário
    """
    return escolha.isnumeric()


"""Função que verifica ganhador no modo tradicional"""
def verificar_tradicional(jogo):
    """matriz para contar quantas peças tem na horizontal"""
    for i in range(len(jogo)):
        cont = [0, 0]
        for j in range(len(jogo[i])):
            if cont[1] >= 4:
                return cont[0]
            elif jogo[i][j]:
                if cont[0] == jogo[i][j]:
                    cont[1] += 1
                else:
                    cont[0] = jogo[i][j]
                    cont[1] = 1
            else:
                cont = [0, 0]

    """matriz para contar quantas peças tem na vertical"""
    for i in range(len(jogo[1])):
        cont = [0, 0]
        for j in range(len(jogo)):
            if jogo[j][i]:
                if cont[0] == jogo[j][i]:
                    cont[1] += 1
                else:
                    cont[0] = jogo[j][i]
                    cont[1] = 1
            else:
                cont = [0, 0]
            if cont[1] >= 4:
                return cont[0]

    """matriz para contar quantas peças tem na diagonal"""
    for i in range(3, len(jogo)):
        for g in range(len(jogo[1]) - 3):
            cont = [0, 0]
            for k in range(4):
                if jogo[i - k][g + k]:
                    if cont[0] == jogo[i - k][g + k]:
                        cont[1] += 1
                    else:
                        cont[0] = jogo[i - k][g + k]
                        cont[1] = 1
                else:
                    break
            if cont[1] >= 4:
                return cont[0]

    return 0

"""Função que verifica ganhador amarelo no modo infinito"""
def verificar_infinito_y(jogo, jogador):
    """matriz para contar quantas peças tem na horizontal"""
    global contador1, circulo_y, c4, c5, c6
    for i in range(len(jogo)):
        cont = [0, 0]  # Matriz para contar quantas pecas tem na horizontal
        for j in range(len(jogo[i])):
            if jogo[i][j] == circulo_y:
                if cont[0] == jogo[i][j]:
                    cont[1] += 1
                else:
                    cont[0] = jogo[i][j]
                    cont[1] = 1
            else:
                cont = [0, 0]
            if c4 == 0:
                if cont[1] == 4 and jogador == JOG1:
                    contador1 += 1
                    c4 += 1
            else:
                if cont[1] == 4 and jogador == JOG1:
                    if cont == ['\x1b[33m●\x1b[0m', 4]:
                        contador1 += 0
                    else:
                        contador1 += 1

    """matriz para contar quantas peças tem na vertical"""
    for i in range(len(jogo[1])):
        cont = [0, 0] # Matriz para contar quantas pecas tem na vertical
        for j in range(len(jogo)):
            if jogo[j][i] == circulo_y:
                if cont[0] == jogo[j][i]:
                    cont[1] += 1
                else:
                    cont[0] = jogo[j][i]
                    cont[1] = 1
            else:
                cont = [0, 0]
            if c5 == 0:
                if cont[1] == 4 and jogador == JOG1:
                    contador1 += 1
                    c5 += 1
            else:
                if cont[1] == 4 and jogador == JOG1:
                    if cont == ['\x1b[33m●\x1b[0m', 4]:
                        contador1 += 0
                    else:
                        contador1 += 1

    """matriz para contar quantas peças tem na diagonal"""
    for i in range(3, len(jogo)): # lembrar que coloquei 3, pois começa a contar do 0
        for g in range(len(jogo[1]) - 3):
            cont = [0, 0]  # matriz para contar quantas pecas tem na diagonal
            for k in range(4):
                if jogo[i - k][g + k] == circulo_y:
                    if cont[0] == jogo[i - k][g + k]:
                        cont[1] += 1
                    else:
                        cont[0] = jogo[i - k][g + k]
                        cont[1] = 1
                else:
                    break
            if c6 == 0:
                if cont[1] == 4 and jogador == JOG1:
                    contador1 += 1
                    c6 += 1
            else:
                if cont[1] == 4 and jogador == JOG1:
                    if cont == ['\x1b[33m●\x1b[0m', 4]:
                        contador1 += 0
                    else:
                        contador1 += 1

    print("Pontuação Jogador {}: {}".format(nome1, contador1))
    print("Pontuação Jogador {}: {}".format(nome2, contador2))

"""Função que verifica ganhador vermelho no modo infinito"""
def verificar_infinito_red(jogo, jogador):
    """matriz para contar quantas peças tem na horizontal"""
    global contador2, circulo_r, c1, c2, c3, ganhou
    for i in range(len(jogo)):
        cont2 = [0, 0]  # Matriz para contar quantas pecas tem na horizontal
        for j in range(len(jogo[i])):
            if jogo[i][j] == circulo_r:
                if cont2[0] == jogo[i][j]:
                    cont2[1] += 1
                else:
                    cont2[0] = jogo[i][j]
                    cont2[1] = 1
            else:
                cont2 = [0, 0]
            if c1 == 0:
                if cont2[1] == 4 and jogador == JOG2:
                    contador2 += 1
                    c1 += 1
            else:
                if cont2[1] == 4 and jogador == JOG2:
                    if cont2 == ['\x1b[31m●\x1b[0m', 4]:
                        contador2 += 0
                    else:
                        contador2 += 1


    """matriz para contar quantas peças tem na vertical"""
    for i in range(len(jogo[1])):
        cont2 = [0, 0]  # Matriz para contar quantas pecas tem na vertical
        for j in range(len(jogo)):
            if jogo[j][i] == circulo_r:
                if cont2[0] == jogo[j][i]:
                    cont2[1] += 1
                else:
                    cont2[0] = jogo[j][i]
                    cont2[1] = 1
            else:
                cont2 = [0, 0]
            if c2 == 0:
                if cont2[1] == 4 and jogador == JOG2:
                    contador2 += 1
                    c2 += 1
            else:
                if cont2[1] == 4 and jogador == JOG2:
                    if cont2 == ['\x1b[31m●\x1b[0m', 4]:
                        contador2 += 0

    """matriz para contar quantas peças tem na diagonal"""
    for i in range(3, len(jogo)): # lembrar que coloquei 3, pois começa a contar do 0
        for g in range(len(jogo[1]) - 3):
            cont2 = [0, 0]  # matriz para contar quantas pecas tem na diagonal
            for k in range(4):
                if jogo[i - k][g + k] == circulo_r:
                    if cont2[0] == jogo[i - k][g + k]:
                        cont2[1] += 1
                    else:
                        cont2[0] = jogo[i - k][g + k]
                        cont2[1] = 1
                else:
                    break
            if c3 == 0:
                if cont2[1] == 4 and jogador == JOG2:
                    contador2 += 1
                    c3 += 1
            else:
                if cont2[1] == 4 and jogador == JOG2:
                    if cont2 == ['\x1b[31m●\x1b[0m', 4]:
                        contador2 += 0

    print("Pontuação Jogador {}: {}".format(nome1, contador1))
    print("Pontuação Jogador {}: {}".format(nome2, contador2))