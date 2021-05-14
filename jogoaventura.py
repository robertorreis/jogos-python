def jogar():
    imprime_abertura()
    esplic_jogo()
    um_pergunta = pergunta_um()


    while um_pergunta <1 or um_pergunta >3:
        print("ESSA OPÇÃO NÃO EXISTE!!")
        um_pergunta = pergunta_um()
    if(um_pergunta == 1):
        print("Você é um festeiro então e gosta da bagunça!!")
        dois_um = pergunta_um_dois()
        if(dois_um == 1):
            print("******PARABÉNS PAPAI!!!!******")
            tres_um = pergunta_um_tres()
            if(tres_um == 1):
                print("Ainda vejo futuro em você!! Talvez você ainda se salve!!")
            else:
                print("FDP você vai para o inferno!!! HAHAHAHAHAHA")

    print("***********************************************")
    print("***************FIM DE JOGO*********************")
    print("***********************************************")

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
    resp = int(input("(1) Gastaria tudo em Festas! (2) Ajudaria Pessoas em Dificuldades (3) Gastaria e também ajudaria:\n"))
    return resp

def pergunta_um_dois():
    print("#############################################")
    print("#############################################")
    print("Vamos continuar a aventura!")
    print("Já que você escolheu a opção (1) sabermos que temos um festeiro e que pode passar pelas seguintes situações:\n")
    print("(1) Engravidar umas desconhecidas nestas festas e ter que começar a dividir o seu $$$")
    print("(2) Passar mau em uma destas festas por estar aproveitando demais se é que você me entende e ir parar em um hospital")
    print("(3) Acordar com pessoas que você nunca viu e em um lugar que você desconhece")
    resp = int(input("Então nos diga digitando uma das opções acima e que poderia acontecer ou talvez perdo disso:\n"))
    return resp

def pergunta_um_tres():
    print("#############################################")
    print("#############################################")
    print("Já que você é o Papai do ano você tem duas opções para continuar nesta aventura que são:\n")
    resp = int(input("(1) Virar um Papai 'responsa' e cuidar dos filhos ou (2) Que se FODA!! EU QUERO FESTA!!!!\n"))
    return resp

if (__name__ == "__main__"):
    jogar()