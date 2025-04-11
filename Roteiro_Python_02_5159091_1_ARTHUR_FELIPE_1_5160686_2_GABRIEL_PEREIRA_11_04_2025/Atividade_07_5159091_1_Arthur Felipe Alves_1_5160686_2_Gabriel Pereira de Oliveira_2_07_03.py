'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 07/03/2025
 ATIVIDADE: Atividade 01
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: SEXTA1
 Nome do arquivo: Atividade_01_5159091_1_5160686_2_07_03.py

'''

def celsius_para_fahrenheit(c):
    return c * (9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * (5/9)

def kelvin_para_celsius(k):
    return k - 273.15

def celsius_para_kelvin(c):
    return c + 273.15

print("=====================Conversor de Temperaturas==================")
print("1: Celsius para Fahrenheit")
print("2: Fahrenheit para Celsius")
print("3: Kelvin para Celsius")
print("4: Celsius para Kelvin")

opcao = int(input("Escolha a conversão desejada (1-4): "))

if opcao == 1:
    c = float(input("Digite a temperatura em Celsius: "))
    print("Temperatura em Fahrenheit: ", celsius_para_fahrenheit(c)," °F")
elif opcao == 2:
    f = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"Temperatura em Celsius:", fahrenheit_para_celsius(f)," °C")
elif opcao == 3:
    k = float(input("Digite a temperatura em Kelvin: "))
    print(f"Temperatura em Celsius: ", kelvin_para_celsius(k)," °C")
elif opcao == 4:
    c = float(input("Digite a temperatura em Celsius: "))
    print(f"Temperatura em Kelvin: ", celsius_para_kelvin(c)," K")
else:
    print("Opção inválida. Escolha um número entre 1 e 4.")
