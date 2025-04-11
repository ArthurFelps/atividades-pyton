'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 14
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_14_5159091_1_5160686_2_10_04.py
'''

def converter_temperatura(valor, origem, destino):

    if origem == "C":
        temp_c = valor
    elif origem == "F":
        temp_c = (valor - 32) * 5/9
    elif origem == "K":
        temp_c = valor - 273.15
    else:
        return "Escala de origem inválida."

    # Converte de Celsius para a escala de destino
    if destino == "C":
        return temp_c
    elif destino == "F":
        return temp_c * 9/5 + 32
    elif destino == "K":
        return temp_c + 273.15
    else:
        return "Escala de destino inválida."


# Programa principal
print("=== Conversor de Temperatura ===")
valor = float(input("Digite o valor da temperatura: "))
origem = input("Digite a escala de origem (C, F ou K): ").upper()
destino = input("Digite a escala de destino (C, F ou K): ").upper()

resultado = converter_temperatura(valor, origem, destino)

if isinstance(resultado, str):
    print("Erro:", resultado)
else:
    print(f"{valor:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
