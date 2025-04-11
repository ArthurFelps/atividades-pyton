'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 13
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_13_5159091_1_5160686_2_10_04.py
'''

import random
import string

def gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos):
    caracteres = ""
    
    if maiusculas:
        caracteres += string.ascii_uppercase  
    if minusculas:
        caracteres += string.ascii_lowercase  
    if numeros:
        caracteres += string.digits  
    if simbolos:
        caracteres += string.punctuation  

    if not caracteres:
        print("Você deve selecionar pelo menos um tipo de caractere!")
        return None

    
    senha = []
    if maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if minusculas:
        senha.append(random.choice(string.ascii_lowercase))
    if numeros:
        senha.append(random.choice(string.digits))
    if simbolos:
        senha.append(random.choice(string.punctuation))

   
    senha += random.choices(caracteres, k=tamanho - len(senha))


    random.shuffle(senha)

    return "".join(senha)


while True:
    try:
        tamanho = int(input("Digite o tamanho da senha (entre 8 e 16): "))
        if 8 <= tamanho <= 16:
            break
        else:
            print("O tamanho deve estar entre 8 e 16.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")


maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
minusculas = input("Incluir letras minúsculas? (s/n): ").strip().lower() == 's'
numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

senha = gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos)

if senha:
    print(f"\nSenha gerada: {senha}")
