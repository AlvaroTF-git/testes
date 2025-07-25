def interface():
    print("      0    1    2          ")
    print(f" 0   [{tabuleiro[0][0]}] [{tabuleiro[0][1]}] [{tabuleiro[0][2]}]")
    print(f" 1   [{tabuleiro[1][0]}] [{tabuleiro[1][1]}] [{tabuleiro[1][2]}]")
    print(f" 2   [{tabuleiro[2][0]}] [{tabuleiro[2][1]}] [{tabuleiro[2][2]}]")

tabuleiro = ([['','','']],
             [['','','']],
             [['','','']]
             )
rodada = "X"

while True:
    interface()
    if rodada == "X":
        Linha = int(input("Digite a linha escolhida: "))
        Coluna = int(input("Digite a coluna escolhida: "))
        tabuleiro[Linha][Coluna] = "X"
    interface()
    rodada = "O"
    if rodada == "O":
        Linha = int(input("Digite a linha escolhida: "))
        Coluna = int(input("Digite a coluna escolhida: "))
        tabuleiro[Linha][Coluna] = "O"
    interface()
    rodada = "X"
    break


