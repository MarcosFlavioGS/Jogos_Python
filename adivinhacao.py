import random #biblioteca importada para possibilitar a geração aleatória de um pseudo número
#Se chama de pseudo número pois, devido à característica determinística do computador, o valor gerado não é exatamente aleatório, mas sim baseado numa "seed".
#"Seeds" podem ser chamadas antes das funções random com a função random.seed(100) com o valor da "seed"dentro dos parenteses. Fazendo que o valor do random definido em seguida seja sempre o mesmo
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    inicio = 1

    while(inicio == 1):

        #Variaveis
        numero_secreto = random.randrange(1,101) #Sempre ver a documentação das bibliotecas para ver as diversas opções das funções
        tentativas = 0
        rodada = 1 #Comentada porque ao invés de while, trocamos para o "for" e este conta as rodadas do jogo
        pontos = 1000

        #print(numero_secreto) #Podemos descomentar este print pra visualizarmos o número secreto para um controle de teste

        print("Escolha a dificuldade:")
        print("(1) Fácil (2) Médio (3) Difícil")
        dificuldade = int(input("Dificuldade:" ))

        if(dificuldade == 1):
            tentativas = 20
        elif(dificuldade == 2):
            tentativas = 10
        elif(dificuldade == 3):
            tentativas = 5    

        #inicio = 1

        #for rodada in range (1, tentativas+1): #(trocado posteriormente o while por for)#While serve como um If, porém este repete o bloco enquanto o que recebe for verdadeiro
        while (rodada <= tentativas):    
            print("Tentativa {} de {}".format( rodada, tentativas )) #String Interpolation #Para mudar a ordem dos parametros dentro das chaves basta colocar o número representante dentro das chaves({1} e {0})
            #Depois relembrar as várias formas de usar o ".format" para organizar casas decimais ou zeros em números inteiros({:d} para inteiros{:f} para flutuantes float)
            chute_string = input("Digite um Número de 1 a 100:")
            chute = int(chute_string) #Converte o tipo de String para Inteiro
            print("Você Respondeu:" , chute_string)

            if(chute < 1 or chute > 100):#Além de "or", existe também a variante "and" para adicionar uma condição
                print("Chute um número de 1 a 100!!")
                continue#continue é um irmão do "break" mas que serve para pular para a próxima iteração(Iteração mesmo)

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print("Acerto Miseravi! {} pontos pra você".format(pontos))
                print("Fim de jogo")
                print("Deseja jogar de novamente ?")
                print("(1)Sim (2)Não")
                escolha = int(input())
                if(escolha == 1):
                    inicio = 1
                    break
                elif(escolha == 2):
                    inicio = 2
                    break#comando comum que interrompe o laço após, neste caso, a confirmação do "if"
            else:
                if(maior):
                    print("Errrou! O seu chute foi maior que o numero secreto.")
                elif(menor):#Elif é uma junção de If e Else, mas serve para fazer com que somente uma das verificações seja rodada
                    print("Errrrou! O seu chute foi menor que o numero secreto.")  
                pontos_perdidos = abs(numero_secreto) - chute
                pontos -= pontos_perdidos      

            rodada = rodada + 1 #comentado porque o "for" já faz a incrementação
    else:
        print("Fim de Jogo")  
if(__name__ == "__main__"):
    jogar()              