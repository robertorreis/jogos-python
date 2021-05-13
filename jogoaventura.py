def jogar():
    imprime_abertura()
    esplic_jogo()
    um_pergunta = pergunta_um()

    while um_pergunta <1 or um_pergunta >3:
        print("ESSA OPÇÃO NÃO EXISTE!!")
        um_pergunta = pergunta_um()
    if(um_pergunta == 1):
        pergunta_um_dois()


def imprime_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Aventura!")
    print("*********************************")

def esplic_jogo():
    print("Vamos Começar a Aventura!")
    print("O Jogo de Aventura será baseado em cima de suas escolhas.")
    print("Conforme as respostas escolhidas nos chegaremos no seu final!!")

def pergunta_um():
    print("###################################")
    print("O que você faria com R$ 1.00000,00?")
    print("Escolha as opções abaixo:")
    resp = int(input("(1) Gastaria tudo em Festas! (2) Ajudaria Pessoas em Dificuldades (3) Gastaria e também ajudaria \n"))
    return resp

def pergunta_um_dois():
    print("Você é um festeiro então e gosta da bagunça!!")


if (__name__ == "__main__"):
    jogar()