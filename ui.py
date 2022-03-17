from jogo import *
import constantes
from constantes import *

def modos():
    '''Seleção do modo de jogo'''
    global modo
    while True:
        modo = input("SELECIONE O MODO QUE DESEJA JOGAR (1=TRADICIONAL / 2=INFINITO): ")
        if modo == "1" or modo == "2":
            break
        else:
            print(colored("PARA SELECIONAR O MODO, INSIRA APENAS O NÚMERO 1 OU 2", "red"))


def main_tradicional():
    """Laço do modo tradicional"""
    constantes.jogo = ini_matriz(tamanho)
    turno = inicia_turno()

    while not constantes.ganhou:
        if turno == JOG1:
            nome = colored(nome1, "yellow")
        else:
            nome = colored(nome2, "red")
        mostra_matriz(constantes.jogo)
        print(colored('Quem vai jogar agora é o jogador {}!'.format(nome), "green"))
        print('Escolha em qual coluna você quer jogar (escolha de 1 a ', tamanho[1], '): ')
        escolha = input()
        while True:
            if jogada_formato_valido(escolha) == True:
                break
            else:
                print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                escolha = input()
        escolha = int(escolha)

        while escolha < 1 or escolha > tamanho[1]:
            print(colored("Número inválido.", "red"))
            print("Escolha em qual coluna você quer jogar (escolha de 1 a ", tamanho[1], "): ")
            escolha = input()
            while True:
                if jogada_formato_valido(escolha) == True:
                    break
                else:
                    print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                    escolha = input()
            escolha = int(escolha)

        if turno == JOG1:
            jogo = jogada(constantes.jogo, escolha - 1, circulo_y)
        else:
            jogo = jogada(constantes.jogo, escolha - 1, circulo_r)

        constantes.ganhou = verificar_tradicional(jogo)
        turno = troca_turno(turno)

    def ganhador():
        """define ganhador do modo tradicional"""
        if constantes.ganhou == circulo_y:
            constantes.ganhador = colored(nome1, "yellow")
        if constantes.ganhou == circulo_r:
            constantes.ganhador = colored(nome2, "red")
        print('O jogador {} venceu!'.format(constantes.ganhador))

    mostra_matriz(constantes.jogo)
    print()
    ganhador()
    return 0


def main_infinito():
    """Laço do modo infinito"""
    constantes.jogo = ini_matriz(tamanho)
    turno = inicia_turno()
    while not constantes.ganhou:
        if turno == JOG1:
            nome = colored(nome1, "yellow")
        else:
            nome = colored(nome2, "red")
        mostra_matriz(constantes.jogo)
        print(colored('Quem vai jogar agora é o jogador {}!'.format(nome), "green"))
        print('Escolha em qual coluna você quer jogar (escolha de 1 a ', tamanho[1], '): ')
        escolha = input()
        while True:
            if jogada_formato_valido(escolha) == True:
                break
            else:
                print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                escolha = input()

        escolha = int(escolha)
        while escolha < 1 or escolha > tamanho[1]:

            print(colored("Número inválido.", "red"))
            print("Escolha em qual coluna você quer jogar (escolha de 1 a ", tamanho[1], "): ")
            escolha = input()
            while True:
                if jogada_formato_valido(escolha) == True:
                    break
                else:
                    print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                    escolha = input()
            escolha = int(escolha)
        if turno == JOG1:
            constantes.jogo = jogada(constantes.jogo, escolha - 1, circulo_y)
        if turno == JOG2:
            constantes.jogo = jogada(constantes.jogo, escolha - 1, circulo_r)

        if turno == JOG1:
            verificar_infinito_y(constantes.jogo, turno)
        else:
            verificar_infinito_red(constantes.jogo, turno)

        print("Pontuação Jogador {}: {}".format(constantes.nome1, constantes.contador1))
        print("Pontuação Jogador {}: {}".format(constantes.nome2, constantes.contador2))

        turno = troca_turno(turno)
        constantes.jogadas += 1

        if len(constantes.pontos1) == 3:
            constantes.ganhou = 1
        if len(pontos2) == 3:
            constantes.ganhou = 1


        limite = tamanho[0] * tamanho[1]
        if constantes.jogadas == limite:
            constantes.ganhou = 1

    mostra_matriz(constantes.jogo)


    if constantes.ganhou == 1:
        if len(pontos1) > len(pontos2):
            constantes.vencedor = nome1
        if len(pontos1) == len(pontos2):
            constantes.vencedor = "empatou"
        if len(pontos2) > len(pontos1):
            constantes.vencedor = nome2

    if constantes.vencedor == "empatou":
        print("O jogo empatou!")
    else:
        print("O vencedor foi o jogador: {}!".format(vencedor))

    return 0


modos()

global modo
if modo == "1":
    print(colored("### \n"
        "COMO JOGAR: \n"
        "O objetivo do jogo é um dos jogadores fazer uma sequência \n"
        "de 4 peças da mesma cor, essa sequência pode ser formada \n"
        "de forma vertical, horizontal ou diagonal. Ganha o jogador \n"
        "que conseguir realizar o objetivo primeiro. \n"
        "###", "green"))
    main_tradicional()
if modo == "2":
    print(colored("### \n"
        "COMO JOGAR: \n"
        "O objetivo principal do jogo é fazer a maior quantidade \n"
        "de sequências de 4 peças da mesma cor, contudo, cada jogador \n"
        "só poderá fazer apenas uma sequência em cada direção (vertical \n"
        "horizontal e diagonal). Ganha o jogador que ao fim de todos os \n"
        "espaços do tabuleiro, tiver a maior quantidade de pontos \n"
        "###", "green"))
    main_infinito()