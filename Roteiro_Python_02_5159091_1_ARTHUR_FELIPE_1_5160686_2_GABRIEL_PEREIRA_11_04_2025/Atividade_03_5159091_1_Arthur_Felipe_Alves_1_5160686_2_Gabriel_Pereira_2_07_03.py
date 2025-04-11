'''
 5159091: Arthur Felipe Alves
 5160686: Gabriel Pereira de Oliveira
 DATA: 07/03/2025
 ATIVIDADE: Atividade 03
 ROTEIRO: ROTEIRO_PYTHON_02
 TURMA: SEXTA1
 Nome do arquivo: Atividade_03_5159091_1_5160686_2_07_03.py

'''

import numpy as np

def encontrar_coordenadas(pts, dists):
    
    (x1, y1), (x2, y2), (x3, y3) = pts
    d1, d2, d3 = dists

    # Montando o sistema de equações
    A = np.array([
        [2 * (x2 - x1), 2 * (y2 - y1)],
        [2 * (x3 - x1), 2 * (y3 - y1)]
    ])
    
    B = np.array([
        [d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2],
        [d1**2 - d3**2 - x1**2 + x3**2 - y1**2 + y3**2]
    ])

    resultado = np.linalg.solve(A, B)
    
    return resultado[0][0], resultado[1][0]

pontos_referencia = [(0, 0), (0, 100), (100, 0)] 
distancias = [50, 70, 80] 

x, y = encontrar_coordenadas(pontos_referencia, distancias)
print(f"Coordenadas do baú: X = {x:.2f}, Y = {y:.2f}")
