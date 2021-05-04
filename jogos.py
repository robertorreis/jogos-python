import jogoforca
import jogoadivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu Jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo?\n"))

    while jogo <1 or jogo >2:
        jogo = int(input("Opção de jogo não existe. Escolha o seu jogo com as opções (1) Forca (2) Adivinhação:\n"))

    if(jogo == 1):
        print("Sua Escolha foi o jogo Forca")
        jogoforca.jogar()
    elif(jogo == 2):
        print("Sua Escolha foi o jogo Adivinhação")
        jogoadivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()