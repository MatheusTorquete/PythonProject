import forca
import advinhacao

def escolhe_jogo():
    print("*********************************")
    print("***Escolha o seu jogo***")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo"))

    if(jogo ==1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
    advinhacao.jogar()

if(__name__ == "__main__"): # verifica se é o arquivo principal para escolher
    escolhe_jogo()
