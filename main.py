# Qual o ano de lançamento do Windows 8?
# Qual a empresa que desenvolveu o Windows 8?
# Windows 8 suporta 2 processadores?
# O Windows 8 pode funcionar com 2 ou mais usuários?
# O que a maioria dos usuários fizeram ao perceber a dificuldade ao usar o Windows 8?

from random import *
from helpbr import *
from os import system
# from pyautogui import hotkey

perguntas = dict()
perguntas[1] = ['2012', 'Qual o ano de lançamento do Windows 8?', ['2005', '2012', '2010', '2019']]
perguntas[2] = ['Microsoft', 'Qual a empresa que desenvolveu o Windows 8?', ['Nasa', 'Intel', 'Google', 'Microsoft']]
perguntas[3] = ['Sim', 'Windows 8 suporta 2 processadores?', ['Não', 'Sim']]
perguntas[4] = ['Não', 'O Windows 8 pode funcionar apenas com 1 usuário?', ['Não', 'Sim']]
perguntas[5] = ['Downgrade', 'O que a maioria dos usuários fizeram ao perceber a dificuldade ao usar o Windows 8?',
                ['Upgrade', 'Downgrade', 'Instalaram o Windows 9', 'Continuaram a usar o Windows 8']]


# shuffle(perguntas[1][2])
# print(len(perguntas))
def limpa():
    system('cls')
    # hotkey('ctrl', 'l')


while True:
    limpa()

    jogadores = dict()
    perguntasSelecionadas = list()
    # Regra pra adicionar um jogador na base de dados é
    # Nome e Quantidade de perguntas acertadas
    # jogadores[1] = ['Nome', 0]

    # Rodadas
    rodada = 0
    while True:
        limpa()
        titulo("Você prestou atenção?")
        if len(perguntasSelecionadas) == len(perguntas):
            erro_customizado('As perguntas acabaram')
            break
        rodada += 1
        nome = verificar_str('Qual o nome do(a) Jogador(a): ')
        perguntasAcertadas = 0
        lenPerguntas = len(perguntas)

        naoTemMaisPerguntas = False
        pergunta = 0
        opResposta = ''
        while not naoTemMaisPerguntas:
            while True:
                pergunta = randint(1, lenPerguntas)
                if pergunta not in perguntasSelecionadas:
                    break
            # print(f'Pergunta {pergunta}')
            if pergunta not in perguntasSelecionadas:
                perguntasSelecionadas.append(pergunta)
                break
            else:
                naoTemMaisPerguntas = True
        # print(perguntasSelecionadas)
        if naoTemMaisPerguntas:
            break

        sep()
        print(perguntas[pergunta][1])
        shuffle(perguntas[pergunta][2])  # Embaralhando as perguntas
        indexResposta = perguntas[pergunta][2].index(perguntas[pergunta][0])
        alternativas = ['A', 'B', 'C', 'D']
        for a in range(len(perguntas[pergunta][2])):
            print(f'{alternativas[a]} - {perguntas[pergunta][2][a]}')
        sep()
        while True:
            opResposta = verificar_str('Resposta: ').upper()
            if opResposta in alternativas[0:len(perguntas[pergunta][2])]:
                break
            erro_customizado('Alternativa inválida')
        sep()
        if alternativas.index(opResposta) == indexResposta:
            print("Resposta certa!")
            perguntasAcertadas += 1
        else:
            print("Resposta errada!")
        sep()
        jogadores[rodada] = [nome, perguntasAcertadas]
        # ===========================================================
        opRodada = verificar_saida("Você quer fazer mais uma rodada? ['S' = Sim | 'N' Não] ")
        if opRodada == 'N':
            break

    # Mostrar as pontuações
    limpa()
    if len(jogadores) != 0:
        titulo('Resultados')
        print(f'{"Nome":<40}Acertos')
        print(f'{"":_<5}{"":<35}{"":_<5}')
        for player in jogadores.values():
            print(f'{player[0]:.<40}{player[1]}')

    sep()
    # ===========================================================
    opMain = verificar_saida("Você quer fazer mais uma sessão de rodadas? ['S' = Sim | 'N' Não] ")
    if opMain == 'N':
        break
