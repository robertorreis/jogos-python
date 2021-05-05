import random


def jogar():
    imprime_abertura()

    numero_secreto = random.randrange(1,7)

    nivel = escolha_nivel()

    while nivel < 1 or nivel > 2:
        nivel = nivel_errado()

    if (nivel == 1):
        print("Numero do dado é {} :".format(numero_secreto))
    else:
        print("Ok!! Obrigado")

def imprime_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Dados!")
    print("*********************************")


def escolha_nivel():
    print("Você quer Jogar dados?")
    print("(1) sim (2) não ")

    nivel = int(input(""))
    return nivel


def nivel_errado():
    nivel = int(input("Esta opção não existe. Você quer jogar dados (1) sim (2) não : "))
    return nivel


if (__name__ == "__main__"):
    jogar()