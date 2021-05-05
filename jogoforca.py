import random

def jogar():

    imprime_abertura()

    palavra_secreta = carrega_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta]

    erros = 0
    qtd_letras(letras_acertadas)
   
    while(True):

        chute = pede_chute()

        if(chute in palavra_secreta):
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros +=1
            chute_errado(erros)

        if(erros == 7):
            break
        if("_" not in letras_acertadas):
            break
        print(letras_acertadas)
        
    if("_" not in letras_acertadas):
        voce_ganhou(palavra_secreta)
    else:
        voce_errou(palavra_secreta)

    print("Fim do Jogo!!")


def imprime_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def carrega_palavra(nome_arquivo = "palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = str.strip(input("Digite uma letra para adivinhar a palavra:\n"))
    chute = chute.upper()
    return chute

def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def chute_errado(erros):
    print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def voce_ganhou(palavra_secreta):
    print("Você ganhou, parabéns!! A palavra é {}".format(palavra_secreta))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def voce_errou(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra é {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def qtd_letras(letras_acertadas):
    print("A palavra a ser adivinhada contém o número de letras abaixo: ")
    print(letras_acertadas)

if(__name__ == "__main__"):
    jogar()
