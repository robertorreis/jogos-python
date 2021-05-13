import random

def jogar():
    imprime_abertura()

    fim = 5
    cont = 0

    while cont < fim:
        pergunta()

        loop_resp(fim, cont, [carrega_respostas()])
        cont = cont + 1
    else:
        print("Decidido e boa sorte!")


def imprime_abertura():
    print("*********************************")
    print("Bem vindo ao jogo Decida por MIM!")
    print("*********************************")

def pergunta():
    questoes = str(input("Digite sua pergunta:\n"))
    return questoes

def loop_resp(fim, cont, resp_loop):
    for resp in resp_loop:
        print(resp)


def carrega_respostas(nome_arquivo = "respostas.txt"):
    arquivo = open(nome_arquivo, "r")
    respostas = []

    for linha in arquivo:
        linha = linha.strip()
        respostas.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(respostas))
    resp_loop = respostas[numero]
    return resp_loop

if (__name__ == "__main__"):
     jogar()