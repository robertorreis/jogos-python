import random

def jogar():
    imprime_abertura()

    numero_secreto = random.randrange(1,101)
    total_de_tenatativas= 0
    pontos = 1000

    nivel = escolha_nivel()

    while nivel <1 or nivel >3:
        nivel = nivel_errado()
        
    if(nivel == 1):
        total_de_tenatativas = 20
    elif(nivel == 2):
        total_de_tenatativas = 10
    else:
        total_de_tenatativas = 5
        
    for rodada in range (1, total_de_tenatativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tenatativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100! Infelizmente perdeu uma rodada")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos! :)".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O Seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O Seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
    print("Fim do Jogo!!")
    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

def imprime_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def escolha_nivel():
    print("Qual o nível de dificuldade você quer jogar?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o seu nível: "))
    return nivel
    
def nivel_errado():
    nivel = int(input("Este nível não existe. Defina o seu nível com as opções (1) Fácil (2) Médio (3) Difícil: "))
    return nivel

if(__name__ == "__main__"):
    jogar()