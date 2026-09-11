"""
Módulo de Validación y Coherencia Dimensional
"""
from typing import List
def es_matriz_regular(matriz: List[List[float]]) -> bool:
    """Verifica que todas las filas de una matriz tengan la misma longitud."""
    if not matriz or not matriz[0]:
        return False
    longitud_esperada = len(matriz[0])
    return all(len(fila) == longitud_esperada for fila in matriz)
def validar_matrices(cargas: List[List[float]], capacidades: List[List[float]]) -> bool:
    """
    Verifica que las matrices sean regulares, tengan dimensiones idénticas,
    cumplan con el tamaño mínimo (N>=2, M>=2) y respeten los límites físicos
    (pesos >= 0, capacidades > 0).
    """
    if not es_matriz_regular(cargas) or not es_matriz_regular(capacidades):
        return False
    n_cargas, n_capacidades = len(cargas), len(capacidades)
    m_cargas, m_capacidades = len(cargas[0]), len(capacidades[0])
    if n_cargas != n_capacidades or m_cargas != m_capacidades:
        return False
    if n_cargas < 2 or m_cargas < 2:
        return False
    for fila_cargas, fila_capacidades in zip(cargas, capacidades):
        for peso, capacidad in zip(fila_cargas, fila_capacidades):
            if peso < 0 or capacidad <= 0:
                return False
    return True
