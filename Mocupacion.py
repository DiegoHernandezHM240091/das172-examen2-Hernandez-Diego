"""
Módulo de Cálculo de Ocupación y Detección de Sobrecarga
"""

from typing import List, Dict, Tuple, Any

def calcular_ocupacion(cargas: List[List[float]], capacidades: List[List[float]]) -> Dict[str, Any]:
    """
    Calcula el porcentaje de ocupación de cada celda de la bodega de carga
    y detecta aquellas que exceden el 100% de su capacidad máxima segura.
    """
    n = len(cargas)
    m = len(cargas[0])

    matriz_porcentajes: List[List[float]] = []
    celdas_sobrecargadas: List[Tuple[int, int]] = []

    for i in range(n):
        fila_porcentajes: List[float] = []
        for j in range(m):
            porcentaje = (cargas[i][j] / capacidades[i][j]) * 100.0
            fila_porcentajes.append(porcentaje)
            if porcentaje > 100.0:
                celdas_sobrecargadas.append((i, j))
        matriz_porcentajes.append(fila_porcentajes)

    return {
        "matriz_porcentajes": matriz_porcentajes,
        "celdas_sobrecargadas": celdas_sobrecargadas,
    }
