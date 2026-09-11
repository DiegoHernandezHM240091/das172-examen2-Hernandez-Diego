"""
Modulo de Evaluación de Balance y Simetría
"""
from typing import List, Dict, Any

def calcular_pesos_por_fila(cargas: List[List[float]]) -> List[float]:
    """Calcula el peso total de cada fila longitudinal de la matriz de cargas."""
    return [sum(fila) for fila in cargas]

def calcular_desbalance_lateral(cargas: List[List[float]]) -> float:
    """Calcula el desbalance lateral (babor vs. estribor) de la carga."""
    m = len(cargas[0])
    mitad = m // 2

    if m % 2 == 0:
        columnas_izquierda = range(0, mitad)
        columnas_derecha = range(mitad, m)
    else:
        columnas_izquierda = range(0, mitad)
        columnas_derecha = range(mitad + 1, m)

    suma_izquierda = sum(fila[j] for fila in cargas for j in columnas_izquierda)
    suma_derecha = sum(fila[j] for fila in cargas for j in columnas_derecha)

    return abs(suma_izquierda - suma_derecha)

def evaluar_balance(cargas: List[List[float]], tolerancia: float) -> Dict[str, Any]:
    """
    Calcula el vector de pesos longitudinales, el desbalance lateral en kg,
    y determina si dicho desbalance se mantiene dentro de la tolerancia permitida.
    """
    pesos_por_fila = calcular_pesos_por_fila(cargas)
    desbalance_lateral = calcular_desbalance_lateral(cargas)
    balance_ok = desbalance_lateral <= tolerancia

    return {
        "pesos_por_fila": pesos_por_fila,
        "desbalance_lateral": desbalance_lateral,
        "balance_ok": balance_ok,
    }
