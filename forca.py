import random

def mensagem_de_abertura():
    print("************************************")
    print("****Bem vindo ao jogo da forca!****")
    print("************************************")

def criar_palavra_secreta():
    # Forma de fazer a mesma coisa que em baixo mas sem a necessidade de chamar o fechamento do arquivo
        palavras = []
        with open("palavras.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)
        
        #arquivo = open("palavras.txt", "r") # Abriu o arquivo
        #palavras = [] # Criada uma lista vazia

        #for linha in arquivo: # Variavel linha criada para cada elemento dentro do arquivo por meio do laço
            #linha = linha.strip() # Eliminou os espaços e caracteres especiais das palavras no arquivo
            #palavras.append(linha) # Incluiu cada linha/palavra de dentro do arquivo para dentro da lista "palavras"

        #arquivo.close() # Fechado o arquivo
        
        sorteio = random.randrange(0, len(palavras)) #Criada variavel "sorteio" que é = a uma posição aleatória num grupo que vai de 0 a quantidade especificada que é o tamanho da lista, mas que poderia ter sido escrito apenas com 4 que é o número especifico.
        palavra_secreta = palavras[sorteio].upper() # Palavra secret agora é = a variável palavras na posição da lista substituída pelo sorteio, que é uma posição aleatória
        return palavra_secreta

def inicio_letras_acertadas(palavra):
    return ["_" for letra in palavra] #Lista ## LIST COMPREHENSIONS Com o laço "for" DENTRO da lista para adicionar "_" para cada elemento na variavel palavra secreta
    #for letra in palavra_secreta:
            #letras_acertadas.append("_") # Uma outra forma de usar for para adicionar "_" para cada elemento dentro da lista palavra_secreta
def pedir_chute_letras():
    chute = input("Chute uma letra: ")#tentar depois limitar o número de caracteres que o usuário pode digitar
    chute = chute.strip().upper() #"strip()" é uma classe/tipo serve para limpar a string de "espaços"
    return chute

def marcar_chute_letra(chute, palavra_secreta, letras_acertadas, tentativas):
    index = 0 #Posição inicial na lista em variavel para verificar cada posição da lista e ser modificada no final do laço "for"
    for letra in palavra_secreta:
        if(chute == letra):# "upper()" classe/tipo serve para reconhecer o caractere maiúsculo
            letras_acertadas[index] = letra #se o chute corresponder à letra na posição sendo verificada, a variavel "letra" que corresponde à letra na posição verificada, toma o lugar do"_" na posição index atual, seguindo para a proxima na lista
        index += 1
    tentativas -= 1

def jogar():

    retorno = 1
    while(retorno == 1):

        mensagem_de_abertura()
        
        palavra_secreta = criar_palavra_secreta()

        letras_acertadas = inicio_letras_acertadas(palavra_secreta) 
        print(letras_acertadas)

        enforcou = False
        acertou = False
        tentativas = 6

        while(not enforcou and not acertou):

            #print(palavra_secreta) #para testes mais rápidos

            print(f"Você tem {tentativas} tentativas")

            print("Sabe qual é a palavra? Gostaria de chutar?")
            tentar = int(input("(1) Sim (2) Não, quero chutar uma letra: "))

            if(tentar == 1):
                print("Vamos lá então!! Se errar, perde o jogo!!!")
                chute1 = input("Chute a palavra: ")
                chute1 = chute1.strip().upper()

                if(chute1 == palavra_secreta):
                    acertou = True
                    
                else:
                    print("Palavra errada")
                    enforcou = True
                    
            elif(tentar == 2):
                        

                print(f"Você tem {tentativas} tentativas")
                
                chute = pedir_chute_letras()

                if(chute in palavra_secreta):
                    
                    marcar_chute_letra(chute, palavra_secreta, letras_acertadas, tentativas)
                        
                else:
                    tentativas -= 1    

                enforcou = tentativas == 0
                acertou = "_" not in letras_acertadas

                print(letras_acertadas)
            if(acertou):
                print("Você acertou !")
                print(f"Parabéns!! Você fez {tentativas ** 2} pontos")
            elif(enforcou):
                print(f"Que pena, você foi enforcado!!! A palavra era: {palavra_secreta}") 

        print("Você gostaria de jogar novamente ?")
        jogar_novamente = int(input("(1) Sim (2) Não "))

        if(jogar_novamente == 1):
            retorno = 1
        elif(jogar_novamente == 2):
            retorno = 0                      

if(__name__ == "__main__"):
    jogar()