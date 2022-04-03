class Cores:
    erro = '\033[31m'
    fim = '\033[0m'


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def sep():
    print('=-' * 20, end='=')
    print()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Titles
def titulo(value):
    sep()
    print(f'{value:^40}')
    sep()


def titulo_personalizado(value):
    print('=-' * (len(value) + 1), end='=')
    print()
    print(f'{value:^{(len(value) * 2) + 2}}')
    print('=-' * (len(value) + 1), end='=')
    print()


def titulo_simples(value):
    print(f'{value:^40}')


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Erros
def erro():
    print(f'{Cores.erro}ERRO: Valor Inválido!{Cores.fim}')


def erro_customizado(value):
    print(f'{Cores.erro}{value}{Cores.fim}')


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Funções para verificar os 3 tipos de dados_antigos que o usuário pode digitar
def verificar_str(questao):
    while True:
        verificar = str(input(questao))
        try:
            int(verificar)
            erro()
        except ValueError:
            break
    return verificar


def verificar_int(questao):
    while True:
        try:
            verificar = int(input(questao))
            break
        except ValueError:
            erro()
    return verificar


def verificar_float(questao):
    while True:
        try:
            verificar = float(input(questao))
            break
        except ValueError:
            erro()
    return verificar
# Funções para verificar os 3 tipos de dados_antigos que o usuário pode digitar


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Verificando a saida do usuário no loop do main do programa
def verificar_saida(questao):
    while True:
        try:
            verificar = str(input(questao)).upper()
            if verificar in 'SN':
                break
            else:
                erro()
        except ValueError:
            erro()
    return verificar
# Verificando a saida do usuário no loop do main do programa


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Matematica
