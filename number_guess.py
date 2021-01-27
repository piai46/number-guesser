import random

lista_tentativas = []

def mostrar_pontuacao():
    #Funcao somente para armazenar as tentivas e mostra-las
    if len(lista_tentativas) <= 0:
        print("Nao tem nenhuma pontuacao registrada, jogue para ser o melhor!")
    else:
        print(f'O mais rapido a adivinhar o numero foi com {min(lista_tentativas)} tentativa(s)!')

def comecar_jogo():
    #Pegando nome do jogador
    nome_jogador = input("Olá!\nQual seu nome caro colega?\n")
    print(f'Seja bem-vindo {nome_jogador}, é uma honra ter voce jogando este jogo!')
    #Randomizando um numero
    numero_sorteado = random.randrange(1, 100)
    #Entrada para comecar ou nao a jogar
    quer_jogar = input("Esta afim de jogar agora? (sim/nao)\n")
    tentativas = 0
    #Mostrando a pontuacao
    mostrar_pontuacao()
    while quer_jogar.lower() == "sim":
        try:
            #Usando try except caso o numero saia do range
            tentativa = int(input("Chute um numero entre 1 e 100\n"))
            tentativas += 1
            if tentativa < 1 or tentativa > 100:
                raise ValueError("Por favor chute um numero entre 1 e 100")
            if tentativa == numero_sorteado:
                #Parabenizando por acertar
                print("Parabéns!", end=" ")
                print(f"Voce acertou com {tentativas} tentativa(s)!")
                #Adicionando a quantidade de tentativas para rankear e mostrar quando acertou mais rapido
                lista_tentativas.append(tentativas)
                mostrar_pontuacao()
                #Perguntando se quer jogar novamente, caso nao queira, o programa fecha
                jogar_novamente = input("Quer jogar outra vez? (sim/nao)\n")
                if jogar_novamente != "sim":
                    print("Beleza entao, have a good one!")
                    break
                numero_sorteado = random.randrange(1, 100)
                tentativas = 0
            elif tentativa > numero_sorteado:
                print("Chute mais baixo!", end=" ")
            elif tentativa < numero_sorteado:
                print("Chute mais alto!", end=" ")
        except ValueError:
            print("Este nao é um valor valido, por favor tente novamente")
    else:
        print("Ok entao, tenha um otimo dia!")

comecar_jogo()