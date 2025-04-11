'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 07/03/2025
 ATIVIDADE: Atividade 02
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: SEXTA1
 Nome do arquivo: Atividade_02_5159091_1_5160686_2_07_03.py

'''

import random

navios = {
    "Porta-aviões": 5,
    "Encouraçado": 4,
    "Destroyer": 3
}
campo_de_batalha = {}
for navio, tamanho in navios.items():
    while True:
        posicao = random.randint(1, 10)
        if posicao not in campo_de_batalha:
            campo_de_batalha[posicao] = {"nome": navio, "vida": tamanho}
            break

navios_restantes = len(navios)

print("\nBATALHA NAVAL INICIADA!")
print("Tente afundar todos os navios inimigos.\n")

while navios_restantes > 0:
    try:
        tiro = int(input("Dispare um tiro (posição de 1 a 10): "))
        
        if tiro < 1 or tiro > 10:
            print("Posição inválida! Escolha um número entre 1 e 10.")
            continue
        
        if tiro in campo_de_batalha:
            navio = campo_de_batalha[tiro]
            navio["vida"] -= 1

            if navio["vida"] == 0:
                print(f"Navio afundado! ({navio['nome']})")
                del campo_de_batalha[tiro]  
                navios_restantes -= 1
            else:
                print("Navio atingido!")
        
        else:
            print("Água!")
        
        print(f"Navios restantes: {navios_restantes}\n")
    
    except ValueError:
        print("Entrada inválida! Digite um número entre 1 e 10.")

print("Parabéns! Você afundou toda a frota inimiga!")