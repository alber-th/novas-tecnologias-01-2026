class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

    def mostrar_tabuleiro(self):
        for i, linha in enumerate(self.tabuleiro):
            print(" | ".join(linha))
            if i < 2:
                print("--+---+--")
                
    def fazer_jogada(self, linha, coluna):
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Posição inválida")
            return

        if self.tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada")
            return

        self.tabuleiro[linha][coluna] = self.jogador_atual

        # Troca o turno
        if self.jogador_atual == "X":
            self.jogador_atual = "O"
        else:
            self.jogador_atual = "X"
            
