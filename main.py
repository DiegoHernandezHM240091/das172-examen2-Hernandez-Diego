"""
Script principal de ejecución.
"""

from Mvalidacion import validar_matrices
from Mocupacion import calcular_ocupacion
from Mbalance import evaluar_balance
from Msubmatriz import extraer_submatriz_critica


def imprimir_matriz(matriz, titulo, decimales=1):
    """Imprime una matriz numérica con formato tabular legible."""
    print(f"\n{titulo}")
    for fila in matriz:
        celdas = [f"{valor:8.{decimales}f}" for valor in fila]
        print("  " + " ".join(celdas))


def imprimir_separador(titulo):
    """Imprime un encabezado de sección para organizar la salida."""
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def ejecutar_demo():
    """Ejecuta el flujo de demostración completo con datos de prueba."""

    # Matriz de cargas reales (kg) - bodega de 4 filas x 5 columnas
    cargas_reales = [
        [420, 380, 500, 410, 390],
        [610, 300, 295, 700, 450],
        [200, 250, 240, 260, 210],
        [500, 480, 300, 320, 510],
    ]

    # Matriz de capacidades máximas (kg) por celda
    capacidades_maximas = [
        [500, 500, 500, 500, 500],
        [600, 400, 400, 600, 500],
        [300, 300, 300, 300, 300],
        [500, 500, 400, 400, 500],
    ]

    tolerancia_desbalance_kg = 150.0
    ventana_k, ventana_p = 2, 2

    imprimir_separador("PASO 1: VALIDACIÓN DIMENSIONAL Y DE COHERENCIA")
    matrices_validas = validar_matrices(cargas_reales, capacidades_maximas)
    print(f"¿Matrices válidas? -> {matrices_validas}")

    if not matrices_validas:
        print("Las matrices de entrada no son válidas. Se detiene la ejecución.")
        return

    imprimir_separador("PASO 2: CÁLCULO DE OCUPACIÓN Y DETECCIÓN DE SOBRECARGA")
    resultado_ocupacion = calcular_ocupacion(cargas_reales, capacidades_maximas)
    imprimir_matriz(
        resultado_ocupacion["matriz_porcentajes"],
        "Matriz de porcentaje de ocupación (%):"
    )
    print(f"\nCeldas en sobrecarga (fila, columna): "
          f"{resultado_ocupacion['celdas_sobrecargadas']}")

    imprimir_separador("PASO 3: EVALUACIÓN DE BALANCE Y SIMETRÍA")
    resultado_balance = evaluar_balance(cargas_reales, tolerancia_desbalance_kg)
    print(f"Peso total por fila (kg): {resultado_balance['pesos_por_fila']}")
    print(f"Desbalance lateral (kg): {resultado_balance['desbalance_lateral']:.2f}")
    print(f"Tolerancia permitida (kg): {tolerancia_desbalance_kg:.2f}")
    print(f"¿Balance dentro de tolerancia? -> {resultado_balance['balance_ok']}")

    imprimir_separador("PASO 4: EXTRACCIÓN DE SUBMATRIZ DE SOBRECARGA CRÍTICA")
    resultado_submatriz = extraer_submatriz_critica(
        resultado_ocupacion["matriz_porcentajes"],
        ventana_k, ventana_p,
        criterio="promedio"
    )
    print(f"Ventana de búsqueda: {ventana_k} x {ventana_p}")
    print(f"Posición de inicio (fila, columna): {resultado_submatriz['posicion']}")
    print(f"Promedio de ocupación de la zona crítica: "
          f"{resultado_submatriz['valor_criterio']:.2f}%")
    imprimir_matriz(
        resultado_submatriz["submatriz"],
        "Submatriz crítica extraída (%):"
    )

    imprimir_separador("RESUMEN FINAL DE AUDITORÍA")
    print(f"Matrices válidas:               {matrices_validas}")
    print(f"Celdas sobrecargadas:          {len(resultado_ocupacion['celdas_sobrecargadas'])}")
    print(f"Balance lateral aprobado:      {resultado_balance['balance_ok']}")
    print(f"Zona crítica más severa en:    fila {resultado_submatriz['posicion'][0]}, "
          f"columna {resultado_submatriz['posicion'][1]}")


if __name__ == "__main__":
    ejecutar_demo()
