def jogar():
    imprime_abertura()
    esplic_jogo()
    pergunta_um()

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
    resp = str.strip(input("(1) Gastaria tudo em Festas! (2) Ajudaria Pessoas em Dificuldades (3) Gastaria e também ajudaria \n"))
    return resp

if (__name__ == "__main__"):
    jogar()