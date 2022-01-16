import adivinhacao
import forca

print ("********************************************")
print("Bem vindo à seleção de jogos super divertidos")
print("*********************************************")

print("escolha o jogo")
print("(1) Jogo da Adivinhação (2) Jogo da Forca")

jogo = int(input())

if(jogo == 1):
    print("Jogando: Adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogando: Forca")
    forca.jogar()    