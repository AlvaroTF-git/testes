def interface():
    print("      0    1    2          ")
    print(f" 0   [{tabuleiro[0][0]}] [{tabuleiro[0][1]}] [{tabuleiro[0][2]}]")
    print(f" 1   [{tabuleiro[1][0]}] [{tabuleiro[1][1]}] [{tabuleiro[1][2]}]")
    print(f" 2   [{tabuleiro[2][0]}] [{tabuleiro[2][1]}] [{tabuleiro[2][2]}]")

tabuleiro = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
rodada = "X"
jogadas = 0

while True:
    if jogadas == 9:
        print("O Jogo empatou!")
        break
    interface()
    if rodada == "X":
        Linha = int(input("Digite a linha escolhida: "))
        Coluna = int(input("Digite a coluna escolhida: "))
        tabuleiro[Linha][Coluna] = "X"
        jogadas = jogadas + 1
    interface()
    rodada = "O"
    if rodada == "O":
        Linha = int(input("Digite a linha escolhida: "))
        Coluna = int(input("Digite a coluna escolhida: "))
        tabuleiro[Linha][Coluna] = "O"
        jogadas = jogadas + 1
    interface()
    rodada = "X"
    


