"""
Pruebas unitarias del Módulo de Evaluación de Balance y Simetría.
"""
import unittest
from Mbalance import (
    evaluar_balance,
    calcular_pesos_por_fila,
    calcular_desbalance_lateral,
)

class TestPesosPorFila(unittest.TestCase):

    def test_pesos_por_fila_tipico(self):
        cargas = [[100, 200, 300], [50, 50, 50]]
        self.assertEqual(calcular_pesos_por_fila(cargas), [600, 150])


class TestDesbalanceLateral(unittest.TestCase):

    def test_columnas_pares_balanceado(self):
        """M par: mitades exactamente iguales -> desbalance 0."""
        cargas = [[100, 100, 100, 100], [50, 50, 50, 50]]
        self.assertEqual(calcular_desbalance_lateral(cargas), 0)

    def test_columnas_pares_desbalanceado(self):
        """M par: mitad derecha con más peso que la izquierda."""
        cargas = [[100, 100, 300, 300]]
        # izquierda = 100+100=200, derecha = 300+300=600 -> |200-600| = 400
        self.assertEqual(calcular_desbalance_lateral(cargas), 400)

    def test_columnas_impares_omite_columna_central(self):
        """M impar: la columna central debe excluirse de la comparación."""
        cargas = [[100, 9999, 100]]
        # columna central (índice 1) se omite; izquierda=100, derecha=100 -> 0
        self.assertEqual(calcular_desbalance_lateral(cargas), 0)

    def test_columnas_impares_desbalance_real(self):
        cargas = [[100, 500, 300]]
        # izquierda=100, derecha=300 (columna central 500 omitida) -> |100-300|=200
        self.assertEqual(calcular_desbalance_lateral(cargas), 200)


class TestEvaluarBalance(unittest.TestCase):

    def test_balance_dentro_de_tolerancia(self):
        cargas = [[100, 100, 120, 100], [100, 100, 100, 100]]
        resultado = evaluar_balance(cargas, tolerancia=50)
        self.assertTrue(resultado["balance_ok"])

    def test_balance_fuera_de_tolerancia(self):
        cargas = [[100, 100, 500, 500]]
        resultado = evaluar_balance(cargas, tolerancia=50)
        self.assertFalse(resultado["balance_ok"])

    def test_desbalance_igual_a_tolerancia_es_aprobado(self):
        """El caso límite (desbalance == tolerancia) debe aprobarse (<=)."""
        cargas = [[100, 200]]  # desbalance = |100-200| = 100
        resultado = evaluar_balance(cargas, tolerancia=100)
        self.assertTrue(resultado["balance_ok"])

    def test_estructura_de_salida_completa(self):
        cargas = [[100, 100], [200, 200]]
        resultado = evaluar_balance(cargas, tolerancia=10)
        self.assertIn("pesos_por_fila", resultado)
        self.assertIn("desbalance_lateral", resultado)
        self.assertIn("balance_ok", resultado)

    def test_no_muta_matriz_de_entrada(self):
        cargas = [[100, 200], [300, 400]]
        cargas_copia = [fila[:] for fila in cargas]
        evaluar_balance(cargas, tolerancia=50)
        self.assertEqual(cargas, cargas_copia)


if __name__ == "__main__":
    unittest.main()
