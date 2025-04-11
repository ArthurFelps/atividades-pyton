'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 07/03/2025
 ATIVIDADE: Atividade 05
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: SEXTA1
 Nome do arquivo: Atividade_05_5159091_1_5160686_2_07_03.py

'''

import random

# Lista de palavras possíveis
PALAVRAS = ["banana", "morango", "abacate", "uva", "laranja", "cereja", "kiwi", "manga"]

# Desenhos da forca conforme o número de erros (6 no total)
FORCA = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]

# Escolhe uma palavra aleatória
def escolher_palavra():
    return random.choice(PALAVRAS)

# Atualiza a palavra exibida com as letras corretas
def atualizar_palavra(palavra, letras_certas):
    return "".join([letra if letra in letras_certas else "_" for letra in palavra])

# Mostra o status atual do jogo
def exibir_status(palavra_secreta, letras_certas, erros):
    print(FORCA[erros])
    print("\nPalavra:", atualizar_palavra(palavra_secreta, letras_certas))
    print("Letras certas:", " ".join(letras_certas))
    print("Erros:", erros)

# Função principal do jogo
def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    erros = 0
    max_erros = 6

    print("=== JOGO DA FORCA ===")
    print("Descubra a palavra secreta!")
    
    while True:
        exibir_status(palavra, letras_certas, erros)
        letra = input("Chute uma letra: ").lower()

        # Validação simples da entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_certas.append(letra)
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            letras_erradas.append(letra)
            erros += 1
            print(f"Ops! A letra '{letra}' não está na palavra.")

        palavra_atual = atualizar_palavra(palavra, letras_certas)

        # Verifica se ganhou
        if "_" not in palavra_atual:
            exibir_status(palavra, letras_certas, erros)
            print("\n🎉 Parabéns! Você adivinhou a palavra:", palavra)
            break

        # Verifica se perdeu
        if erros >= max_erros:
            exibir_status(palavra, letras_certas, erros)
            print("\n💀 Você perdeu! A palavra era:", palavra)
            break

# Executa o jogo
jogar_forca()
