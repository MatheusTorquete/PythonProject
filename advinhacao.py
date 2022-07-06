import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1,11)
    total_de_tentativas = 0
    pontos = 100

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int (input("Defina o nível: ")) # converteu para tipo int

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1 ,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #.format coloca a informação dentro das chaves


        chute_str = input("Digite um número de 1 até 10: ") # input é sempre string
        print("Você digitou " , chute_str)
        chute = int(chute_str) # conversão para INT

        if (chute < 1 or chute > 10):
            print("Você deve digitar um número de 1 até 10")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)  # pontos perdidos da rodada
            pontos = pontos - pontos_perdidos  # subtraindo os pontos perdidos da pontuação total
            if (maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))


    print("Fim do jogo")

if(__name__ == "__main__"): # verifica para rodar o jogo solo
    jogar()