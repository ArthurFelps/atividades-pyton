'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 10/04/2025
 ATIVIDADE: Atividade 15
 ROTEIRO: ROTEIRO_PYTHON_01
 TURMA: SEXTA1
 Nome do arquivo: Atividade_15_5159091_1_5160686_2_10_04.py
'''

# Constante (taxa mínima para alerta, como exemplo)
TAXA_ALERTA = 0.5  # 50% ao ano, por exemplo

# Função que calcula o valor final com juros compostos
def calcular_juros_compostos(valor_inicial, taxa_juros, tempo):
    valor_final = valor_inicial * (1 + taxa_juros) ** tempo
    return valor_final

# Função principal que organiza a entrada, cálculo e saída
def simular_investimento():
    print("=== Simulador de Investimento com Juros Compostos ===")

    # Entrada do usuário
    valor_inicial_str = input("Digite o valor inicial do investimento (ex: 1000): ")
    taxa_str = input("Digite a taxa de juros (ex: 0.05 para 5%): ")
    tempo_str = input("Digite o tempo do investimento em anos (ex: 3): ")

    # Conversão das strings para tipos apropriados
    valor_inicial = float(valor_inicial_str)
    taxa_juros = float(taxa_str)
    tempo = int(tempo_str)

    # Verificação relacional e lógica simples
    if taxa_juros > TAXA_ALERTA:
        print("Aviso: Essa é uma taxa de juros muito alta!")

    # Cálculo do valor final
    valor_final = calcular_juros_compostos(valor_inicial, taxa_juros, tempo)

    # Exibição formatada do resultado
    print(f"\nResultado do Investimento:")
    print(f"Valor Inicial: R${valor_inicial:.2f}")
    print(f"Taxa de Juros: {taxa_juros * 100:.2f}% ao ano")
    print(f"Tempo: {tempo} anos")
    print(f"Valor Final: R${valor_final:.2f}")

    historico = [valor_inicial, taxa_juros, tempo, valor_final]
    resultado_tupla = tuple(historico)

    print("\nResumo (tupla):", resultado_tupla)

simular_investimento()
