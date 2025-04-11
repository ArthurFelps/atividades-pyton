'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 08
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_08_5159091_1_5160686_2_10_04.py
'''

frase = input("Digite uma frase: ").lower()

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
    if letra in vogais:
        vogais[letra] += 1

for vogal, quantidade in vogais.items():
    print(f"A vogal '{vogal}' aparece {quantidade} vezes")