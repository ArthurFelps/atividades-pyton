'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 11
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_11_5159091_1_5160686_2_10_04.py
'''

texto = input("Digite uma frase: ")

capitalize = " ".join([palavra.capitalize() for palavra in texto.split()])
lowercase = texto.lower()
uppercase = texto.upper()
title = texto.title()

print(f"• Capitalize: {capitalize}")
print(f"• Lowercase: {lowercase}")
print(f"• Uppercase: {uppercase}")
print(f"• Title: {title}")
