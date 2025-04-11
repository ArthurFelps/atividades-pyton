'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 07/03/2025
 ATIVIDADE: Atividade 05
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: SEXTA1
 Nome do arquivo: Atividade_05_5159091_1_5160686_2_07_03.py

'''

def tabuleiro(casas):
    print(f"\n  {casas[0][0]} | {casas[0][1]} | {casas[0][2]}")
    print("  ---------")
    print(f"  {casas[1][0]} | {casas[1][1]} | {casas[1][2]}")
    print("  ---------")
    print(f"  {casas[2][0]} | {casas[2][1]} | {casas[2][2]}\n")

def verifica_vitoria(casas, jogador):
    simbolo = 'X' if jogador == 0 else 'O'
    # Linhas, colunas e diagonais
    return (
        any(all(casas[i][j] == simbolo for j in range(3)) for i in range(3)) or
        any(all(casas[i][j] == simbolo for i in range(3)) for j in range(3)) or
        all(casas[i][i] == simbolo for i in range(3)) or
        all(casas[i][2-i] == simbolo for i in range(3))
    )

def jogo():
    while True:
        casas = [[' ' for _ in range(3)] for _ in range(3)]
        vez = 0
        for _ in range(9):
            tabuleiro(casas)
            jogador = 'X' if vez % 2 == 0 else 'O'
            print(f"Jogador {jogador}")
            
            while True:
                try:
                    l = int(input("Digite a linha (1-3): ")) - 1
                    c = int(input("Digite a coluna (1-3): ")) - 1
                    if 0 <= l < 3 and 0 <= c < 3 and casas[l][c] == ' ':
                        casas[l][c] = jogador
                        break
                    else:
                        print("Posição inválida ou ocupada. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número entre 1 e 3.")
            
            if verifica_vitoria(casas, vez % 2):
                tabuleiro(casas)
                print(f"O Vencedor foi o Jogador {jogador}!")
                break
            
            vez += 1
        else:
            tabuleiro(casas)
            print("Empate!")
        
        res = input("Deseja jogar novamente? (S/N): ").strip().upper()
        if res != 'S':
            break

jogo()