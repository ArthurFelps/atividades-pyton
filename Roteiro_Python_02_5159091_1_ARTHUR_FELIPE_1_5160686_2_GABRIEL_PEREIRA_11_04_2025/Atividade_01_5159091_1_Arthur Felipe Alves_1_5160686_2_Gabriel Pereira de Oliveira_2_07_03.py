'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 07/03/2025
 ATIVIDADE: Atividade 01
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: SEXTA1
 Nome do arquivo: Atividade_01_5159091_1_5160686_2_07_03.py

'''

print("Somente a chave correta abrirá meu segredo. Me diga três números distintos, e revelarei se a soma dos dois maiores é maior que o menor.")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a == b or a == c or b == c:
    print("Os números devem ser distintos!")
else:
    menor = min(a, b, c)
    maiores = sorted([a, b, c])[1:]  
    maior1, maior2 = maiores

    if maior1 + maior2 > menor:
        print(f"Sim, a soma dos dois maiores números {maior1} e {maior2} é maior que o menor {menor}.")
    else:
        print(f"Não, a soma dos dois maiores números {maior1} e {maior2} NÃO é maior que o menor {menor}.")