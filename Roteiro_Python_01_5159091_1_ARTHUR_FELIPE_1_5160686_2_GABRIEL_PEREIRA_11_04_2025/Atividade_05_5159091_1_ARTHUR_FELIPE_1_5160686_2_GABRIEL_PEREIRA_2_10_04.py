'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 05
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_05_5159091_1_5160686_2_10_04.py
'''

frase = input("Digite uma frase: ")

num_caracteres = len(frase)
print(f"Número de caracteres na frase: {num_caracteres}")

# Converter todos os caracteres para letras maiúsculas
frase_maiuscula = frase.upper()
print(f"Frase em maiúsculas: {frase_maiuscula}")

# Substituir uma palavra específica por outra fornecida pelo usuário
palavra_antiga = input("Digite a palavra que deseja substituir: ")
palavra_nova = input("Digite a nova palavra: ")
frase_modificada = frase.replace(palavra_antiga, palavra_nova)
print(f"Frase modificada: {frase_modificada}")

# Dividir a frase em uma lista de palavras e exibi-la
lista_palavras = frase.split()
print(f"Lista de palavras: {lista_palavras}")