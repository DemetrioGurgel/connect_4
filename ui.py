from jogo import *
import constantes
from constantes import *
import banco_de_dados
from termcolor import colored

def modos():
    '''
    Seleção do modo de jogo
    '''
    while True:
        constantes.modo = input("SELECIONE O MODO QUE DESEJA JOGAR (1=TRADICIONAL / 2=INFINITO): ")
        if constantes.modo == "1" or constantes.modo == "2":
            break
        else:
            print(colored("PARA SELECIONAR O MODO, INSIRA APENAS O NÚMERO 1 OU 2", "red"))

def comeca_jogo():
    '''
    Função que executa o save game, caso tenha dados de um jogo anterior, e caso o jogador selecione 1
    '''

    while True:
        continuar = input("SAVE GAME [1] / NEW GAME [2]: ")
        if continuar == "1":
            if banco_de_dados.verifica_memoria():
                banco_de_dados.carrega_jogo()
                mostra_matriz(constantes.jogo)
                break
            else:
                print(colored("Não foram encontrados dados, por favor selecione 2 para jogar um novo jogo", "red"))
        elif continuar == "2":
            constantes.nome1 = input('Digite o nome do primeiro jogador: ')
            constantes.nome2 = input('Digite o nome do segundo jogador: ')
            modos()
            constantes.jogador_atual = 1
            constantes.jogo = ini_matriz(tamanho)
            constantes.turno = inicia_turno()
            break
        else:
            print(colored("Por favor, digite apenas 1 para continuar o jogo salvo, ou 2 para um novo jogo:", "red"))

comeca_jogo()



def main_tradicional():
    """
    Laço do modo tradicional
    """
    while not constantes.ganhou:
        if constantes.turno == JOG1:
            constantes.nome = colored(constantes.nome1, "yellow")
        else:
            constantes.nome = colored(constantes.nome2, "red")
        mostra_matriz(constantes.jogo)
        print(colored('Quem vai jogar agora é o jogador {}!'.format(constantes.nome), "green"))
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

        if constantes.turno == JOG1:
            jogo = jogada(constantes.jogo, escolha - 1, circulo_y)
        else:
            jogo = jogada(constantes.jogo, escolha - 1, circulo_r)

        constantes.ganhou = verificar_tradicional(jogo)
        constantes.turno = troca_turno(constantes.turno)
        banco_de_dados.savegame()

    def ganhador():
        """
        define ganhador do modo tradicional
        :return: retorna o ganhador
        """
        if constantes.ganhou == constantes.circulo_y:
            constantes.ganhador = colored(constantes.nome1, "yellow")
        if constantes.ganhou == constantes.circulo_r:
            constantes.ganhador = colored(constantes.nome2, "red")
        print('O jogador {} venceu!'.format(constantes.ganhador))

    mostra_matriz(constantes.jogo)
    print()
    ganhador()
    return 0


def main_infinito():
    """
    Laço do modo infinito
    """
    while not constantes.ganhou:
        if constantes.turno == constantes.JOG1:
            constantes.nome = colored(constantes.nome1, "yellow")
        else:
            constantes.nome = colored(constantes.nome2, "red")
        mostra_matriz(constantes.jogo)
        print(colored('Quem vai jogar agora é o jogador {}!'.format(constantes.nome), "green"))
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
        if constantes.turno == JOG1:
            constantes.jogo = jogada(constantes.jogo, escolha - 1, circulo_y)
        if constantes.turno == JOG2:
            constantes.jogo = jogada(constantes.jogo, escolha - 1, circulo_r)

        verificar_infinito(constantes.jogo, constantes.turno)


        print("Pontuação Jogador {}: {}".format(constantes.nome1, constantes.contador1))
        print("Pontuação Jogador {}: {}".format(constantes.nome2, constantes.contador2))

        constantes.turno = troca_turno(constantes.turno)
        constantes.jogadas += 1

        if constantes.contador1 == 3:
            constantes.ganhou = 1
        if constantes.contador2 == 3:
            constantes.ganhou = 1


        limite = tamanho[0] * tamanho[1]
        if constantes.jogadas == limite:
            constantes.ganhou = 1

        banco_de_dados.savegame()

    mostra_matriz(constantes.jogo)


    if constantes.ganhou == 1:
        if constantes.contador1 > constantes.contador2:
            constantes.vencedor = colored(constantes.nome1, "yellow")
        if constantes.contador1 == constantes.contador2:
            constantes.vencedor = "empatou"
        if constantes.contador2 > constantes.contador1:
            constantes.vencedor = colored(constantes.nome2, "red")

    if constantes.vencedor == "empatou":
        print("O jogo empatou!")
    else:
        print("O vencedor foi o jogador: {}!".format(constantes.vencedor))

    return 0


if constantes.modo == "1":
    print(colored("### \n"
        "COMO JOGAR: \n"
        "O objetivo do jogo é um dos jogadores fazer uma sequência \n"
        "de 4 peças da mesma cor, essa sequência pode ser formada \n"
        "de forma vertical, horizontal ou diagonal. Ganha o jogador \n"
        "que conseguir realizar o objetivo primeiro. \n"
        "###", "green"))
    main_tradicional()
if constantes.modo == "2":
    print(colored("### \n"
        "COMO JOGAR: \n"
        "O objetivo principal do jogo é fazer a maior quantidade \n"
        "de sequências de 4 peças da mesma cor, contudo, cada jogador \n"
        "só poderá fazer apenas uma sequência em cada direção (vertical \n"
        "horizontal e diagonal). Ganha o jogador que ao fim de todos os \n"
        "espaços do tabuleiro, tiver a maior quantidade de pontos \n"
        "###", "green"))
    main_infinito()