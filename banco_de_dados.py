import pickle
import constantes

def savegame():
    '''
    Função que utiliza o pickle para armazernar as constantes e variáveis do jogo
    :return: retorna True se tiver armazenado dados
    '''
    memoria = open('savegame.pkl', 'wb')

    dados_pra_salvar = (
        1,
        constantes.nome1,
        constantes.nome2,
        constantes.modo,
        constantes.turno,
        constantes.JOG1,
        constantes.JOG2,
        constantes.jogador_atual,
        constantes.c1,
        constantes.c2,
        constantes.c3,
        constantes.c4,
        constantes.c5,
        constantes.c6,
        constantes.jogadas,
        constantes.ganhou,
        constantes.contador1,
        constantes.contador2,
        constantes.jogo,

    )


    pickle.dump(dados_pra_salvar, memoria)

    memoria.close()
    return True


def carrega_jogo():
    '''
    Função para carregar o jogo salvo
    :return: retorna True se tiver carregado os dados
    '''
    memoria = open('savegame.pkl', 'rb')
    dados_salvos = pickle.load(memoria)

    constantes.nome1 = dados_salvos[1]
    constantes.nome2 = dados_salvos[2]
    constantes.modo = dados_salvos[3]
    constantes.turno = dados_salvos[4]
    constantes.JOG1 = dados_salvos[5]
    constantes.JOG2 = dados_salvos[6]
    constantes.jogador_atual = dados_salvos[7]
    constantes.c1 = dados_salvos[8]
    constantes.c2 = dados_salvos[9]
    constantes.c3 = dados_salvos[10]
    constantes.c4 = dados_salvos[11]
    constantes.c5 = dados_salvos[12]
    constantes.c6 = dados_salvos[13]
    constantes.jogadas = dados_salvos[14]
    constantes.ganhou = dados_salvos[15]
    constantes.contador1 = dados_salvos[16]
    constantes.contador2 = dados_salvos[17]
    constantes.jogo = dados_salvos[18]

    memoria.close()
    return True


def verifica_memoria():
    '''
    Função que verifica se existe dados salvos de um jogo anterior
    :return: Retorna True se existir dados, False se caso não exista
    '''
    try:
        memoria = open('savegame.pkl', 'rb')
        dados_salvos = pickle.load(memoria)

        if dados_salvos[0]:
            return True

        return False

    except:
        return False