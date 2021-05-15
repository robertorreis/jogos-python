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
            print("******PARABÉNS PAPAI ou Mamãe!!!!******")
            tres_um = pergunta_um_tres()
            if(tres_um == 1):
                print("Ainda vejo futuro em você!! Talvez você ainda se salve!!")
            else:
                print("FDP você vai para o inferno!!! HAHAHAHAHAHA")
        if(dois_um == 2):
            print("Se deu mau Parça você foi para o hospital!!!!")
            dois_dois = pergunta_dois_um()
            if(dois_dois == 1):
                print("Que MENTIROSO Parça!! Sabemos que você vai continuar na zueira gastando o dinheiro")
                print("Só pra você saber, passou uns dias e você MORREU!!")
            else:
                print("ISSO MESMO PARÇA!!! TEM QUE SER HONESTO COM VOCÊ MESMO E CURTIR A VIDA!!!")
        if(dois_um == 3):
            print("Que Fita Parça!! Se perdeu?? HAHAHAHAHA")
            tres_tres = pergunta_tres_um()
            if(tres_tres == 1):
                print("Que pena parça, você ficou loco e passou sua grana toda para uma instituição de caridade pela net!! Pelo lado bom você tem salvação!!")
            else:
                print("É parça!! Era melhor não ter ido porque agora você sabe que se casou e não vai poder curtir mais a vida!!")
    elif(um_pergunta == 2):
        print("Você é um cara de bom coração!!! Mais será que esta falando a verdade mesmo??")
        um_dois = pergunta_dois()
        if(um_dois == 1):
            print("BOM PELO MENOS VC ESTÁ TENTANDO SER HONESTO")
            um_dois_dois = pergunta_dois_dois()
            if(um_dois_dois == 1):
                print("Boa!!! Está sendo hosnesto e irá ajudar pessoas! VC ESTÁ SALVO NO REINO DE DEUS! HAHAHAHA")
            elif(um_dois_dois == 2):
                print("HUMMMMM! SERÁ QUE PODEMOS ACREDITAR NESTES 50% NÃO ESTAMOS MUITO CERTOS QUE VOCÊ IRÁ FAZER ISSO!! TÁ MENTIDO? DESUS CASTIGA! HAHAHAHA")
            else:
                print("HAHAHAHAHAHAH BOA TENTATIVA DE NOS ENGANAR PENSANDO QUE VAI PRO SEU!! COMEÇA O JOGO NOVAMENTE E ESCOLHE OUTRA OPÇÃO!!!!")
        else:
            print("NÃO MINTA PARA MENTIROSO SABEMOS QUE NÃO VAI FAZER ISSO!! HAHAHAHAHHA")
    else:
        print("VOCÊ É FERA BIXO!!! Isso é ser honesto")


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
    print("O que você faria se ganhasse $ 1.00000,00?")
    print("Escolha as opções abaixo:")
    resp = int(input("(1) Gastaria tudo em Festas! (2) Ajudaria Pessoas em Dificuldades (3) Gastaria e também ajudaria:\n"))
    return resp

def pergunta_um_dois():
    print("#############################################")
    print("#############################################")
    print("Vamos continuar a aventura!")
    print("Já que você escolheu a opção (1) sabermos que temos um festeiro e que pode passar pelas seguintes situações:\n")
    print("(1) Engravidar umas desconhecidas nestas festas e ter que começar a dividir o seu $$$ ou ficar grávida de um cara desconhecido!!")
    print("(2) Passar mau em uma destas festas por estar aproveitando demais se é que você me entende!!")
    print("(3) Acordar com pessoas que você nunca viu e em um lugar que você desconhece")
    resp = int(input("Então nos diga digitando uma das opções acima e que poderia acontecer ou talvez perdo disso:\n"))
    return resp

def pergunta_um_tres():
    print("#############################################")
    print("#############################################")
    print("Já que você é o Papai ou Mamãe do ano você tem duas opções para continuar nesta aventura que são:\n")
    resp = int(input("(1) Virar um Papai/Mamãe 'responsa' e cuidar dos filhos ou (2) Que se FODA!! EU QUERO FESTA!!!!\n"))
    return resp

def pergunta_dois_um():
    print("#############################################")
    print("#############################################")
    print("No hospital você está pensando na vida! E temos algumas opções que poderiam surgir:")
    print("(1) Se eu sair dessa prometo parar com tudo e viver uma vida calma e construir uma familia!!")
    print("(2) Quase fui nessa!! Poxa se eu sair daqui vou aproveitar mais minha vida como se não tivesse amanhã!!")
    resp = int(input("Queremos saber qual dessas vocês decidiria seguir, conte para nos!!!\n"))
    return resp

def pergunta_tres_um():
    print("#############################################")
    print("#############################################")
    print("Já que você acordou e não lembra de nada do que você fez qual seria o seu pensamento:")
    resp = int(input("(1) FODA-SE!! BORA CURTIR SOU RICO MESMO! ou (2) Vou saber o que aconteceu e o que eu fiz!!\n"))
    return resp

def pergunta_dois():
    print("#############################################")
    print("#############################################")
    print("Então borá verificar isso!! Vejamos o que você poderia fazer!!")
    resp = int(input("(1) Administraria o dinheiro ajudando conforme suas pesquisas ou (2) Transferia o dinheiro para um instituição confiavél\n"))
    return resp

def pergunta_dois_dois():
    print("#############################################")
    print("#############################################")
    print("Quanto estaria disposto a doar deste dinheiro:")
    resp = int(input("(1) 30% ou (2) 50% ou (3) 80%\n"))
    return resp

if (__name__ == "__main__"):
    jogar()