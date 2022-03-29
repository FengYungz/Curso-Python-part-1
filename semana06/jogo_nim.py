def computador_escolhe_jogada(n, m):
    comp_remove_peca = 1

    while comp_remove_peca != m:
        if (n - comp_remove_peca) % (m+1) == 0:
            return comp_remove_peca
        else:
            comp_remove_peca += 1

    return comp_remove_peca

def usuario_escolhe_jogada(n, m):
    jogada_valida_jogador = False

    while not jogada_valida_jogador:
        jogador_remove_peca = int(input("Quantas peças você vai tirar? "))
        if jogador_remove_peca < 1 or jogador_remove_peca > m:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            jogada_valida_jogador = True

    return jogador_remove_peca

def campeonato():
    num_rodada = 1
    while num_rodada <= 3:
        print()
        print(f"**** Rodada {num_rodada} ****")
        print()
        partida()
        num_rodada += 1
    print()
    print("Placar: Você 0 X 3 Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    jogada_comp = False

    if n % (m+1) == 0:
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        jogada_comp = True

    while n > 0:
        if jogada_comp:
            comp_remove = computador_escolhe_jogada(n, m)
            n = n - comp_remove
            if comp_remove == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print(f"O computador tirou {comp_remove} peças")

            jogada_comp = False
        else:
            jogador_remove_peca = usuario_escolhe_jogada(n, m)
            n = n - jogador_remove_peca
            if jogador_remove_peca == 1:
                print()
                print("Voce tirou uma peça")
            else:
                print()
                print(f"Voce tirou {jogador_remove_peca} peças.")
            jogada_comp = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print(f"Agora restam {n} peças no tabuleiro")
                print()

    print("Fim do jogo! O computador ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")

escolhepartida = int(input("2 - para jogar um campeonato "))

if escolhepartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if escolhepartida == 1:
        print()
        partida()