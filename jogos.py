import jogoforca
import jogoadivinhacao
import jogodados
import jogodecisao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu Jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Dados (4) Decide por MIM")

    jogo = int(input("Qual Jogo?\n"))

    while jogo <1 or jogo >4:
        jogo = int(input("Opção de jogo não existe. Escolha o seu jogo com as opções (1) Forca (2) Adivinhação (3) Dados (4) Decide por MIM:\n"))

    if(jogo == 1):
        print("Sua Escolha foi o Jogo Forca")
        jogoforca.jogar()
    elif(jogo == 2):
        print("Sua Escolha foi o Jogo Adivinhação")
        jogoadivinhacao.jogar()
    elif(jogo == 3):
        print("Sua Escolha foi o Jogo Dados")
        jogodados.jogar()
    else:
        print("Sua Escolha foi o jogo Decida por MIM")
        jogodecisao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()