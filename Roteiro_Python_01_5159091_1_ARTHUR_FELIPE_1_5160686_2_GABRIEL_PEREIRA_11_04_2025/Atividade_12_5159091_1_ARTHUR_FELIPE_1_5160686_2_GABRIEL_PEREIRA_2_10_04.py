'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 12
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_12_5159091_1_5160686_2_10_04.py
'''

def validar_entrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))  # Permite entrada com vírgula ou ponto
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um número positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

altura = validar_entrada("Digite sua altura em metros (ex: 1.75): ")
peso = validar_entrada("Digite seu peso em kg (ex: 70.5): ")


imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Excesso de peso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade Grau I"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

# Exibe o resultado
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
