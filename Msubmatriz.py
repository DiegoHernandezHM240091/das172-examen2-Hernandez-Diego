"""
Módulo de Extracción de Submatriz de Sobrecarga Crítica
"""

from typing import List, Dict, Any

def _extraer_ventana(
    matriz: List[List[float]], fila_inicio: int, col_inicio: int, k: int, p: int
) -> List[List[float]]:
    """Extrae, sin modificar la matriz original, la submatriz k x p que comienza en (fila_inicio, col_inicio)."""
    return [fila[col_inicio : col_inicio + p] for fila in matriz[fila_inicio : fila_inicio + k]]

def _valor_ventana(ventana: List[List[float]], criterio: str) -> float:
    """
    Calcula el valor de evaluación de una ventana según el criterio:
        - "promedio": promedio de ocupación de la ventana.
        - "conteo_sobrecarga": número de celdas sobrecargadas (>100%).
    """
    valores = [valor for fila in ventana for valor in fila]
    if criterio == "conteo_sobrecarga":
        return float(sum(1 for valor in valores if valor > 100.0))
    return sum(valores) / len(valores) if valores else 0.0


def extraer_submatriz_critica(
    matriz_porcentajes: List[List[float]], k: int, p: int, criterio: str = "promedio"
) -> Dict[str, Any]:
    """
    Recorre todas las submatrices contiguas de tamaño k x p dentro de la
    matriz de porcentajes de ocupación para identificar la zona más crítica.
    """
    n = len(matriz_porcentajes)
    m = len(matriz_porcentajes[0]) if n > 0 else 0

    if k <= 0 or p <= 0:
        raise ValueError("Las dimensiones k y p deben ser mayores que 0.")
    if k > n or p > m:
        raise ValueError("La ventana k x p excede las dimensiones de la matriz N x M.")

    mejor_valor = -1.0
    mejor_submatriz: List[List[float]] = []
    mejor_posicion = (0, 0)

    for fila_inicio in range(n - k + 1):
        for col_inicio in range(m - p + 1):
            ventana = _extraer_ventana(matriz_porcentajes, fila_inicio, col_inicio, k, p)
            valor = _valor_ventana(ventana, criterio)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_submatriz = ventana
                mejor_posicion = (fila_inicio, col_inicio)

    return {
        "submatriz": mejor_submatriz,
        "valor_criterio": mejor_valor,
        "posicion": mejor_posicion,
    }
