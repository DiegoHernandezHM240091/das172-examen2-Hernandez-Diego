"""
Pruebas unitarias del Módulo de Validación y Coherencia Dimensional.
"""

import unittest
from Mvalidacion import validar_matrices, es_matriz_regular


class TestValidarMatrices(unittest.TestCase):

    def test_caso_tipico_valido(self):
        """Dos matrices 3x3 coherentes deben validarse como True."""
        cargas = [[100, 200, 100], [150, 150, 150], [300, 100, 100]]
        capacidades = [[200, 300, 200], [200, 200, 200], [400, 200, 200]]
        self.assertTrue(validar_matrices(cargas, capacidades))

    def test_dimension_minima_2x2_valida(self):
        """El tamaño mínimo permitido (2x2) debe ser aceptado."""
        cargas = [[10, 20], [30, 40]]
        capacidades = [[50, 50], [50, 50]]
        self.assertTrue(validar_matrices(cargas, capacidades))

    def test_dimensiones_no_coincidentes(self):
        """Si N x M de cargas difiere de capacidades, debe ser False."""
        cargas = [[10, 20], [30, 40]]
        capacidades = [[50, 50, 50], [50, 50, 50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_matriz_menor_a_2x2_filas(self):
        """Una matriz con N < 2 (una sola fila) debe ser rechazada."""
        cargas = [[10, 20]]
        capacidades = [[50, 50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_matriz_menor_a_2x2_columnas(self):
        """Una matriz con M < 2 (una sola columna) debe ser rechazada."""
        cargas = [[10], [20]]
        capacidades = [[50], [50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_matriz_irregular_filas_desiguales(self):
        """Filas de longitud desigual (matriz no regular) deben rechazarse."""
        cargas = [[10, 20, 30], [40, 50]]
        capacidades = [[50, 50, 50], [50, 50, 50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_peso_negativo_invalido(self):
        """Un peso negativo debe invalidar la matriz."""
        cargas = [[-5, 20], [30, 40]]
        capacidades = [[50, 50], [50, 50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_peso_cero_es_valido(self):
        """Un peso igual a cero (celda vacía) es válido (>= 0)."""
        cargas = [[0, 20], [30, 40]]
        capacidades = [[50, 50], [50, 50]]
        self.assertTrue(validar_matrices(cargas, capacidades))

    def test_capacidad_cero_invalida(self):
        """Una capacidad igual a cero debe invalidar la matriz (> 0 requerido)."""
        cargas = [[10, 20], [30, 40]]
        capacidades = [[0, 50], [50, 50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_capacidad_negativa_invalida(self):
        """Una capacidad negativa debe invalidar la matriz."""
        cargas = [[10, 20], [30, 40]]
        capacidades = [[-10, 50], [50, 50]]
        self.assertFalse(validar_matrices(cargas, capacidades))

    def test_matriz_vacia_invalida(self):
        """Matrices vacías deben ser rechazadas."""
        self.assertFalse(validar_matrices([], []))

    def test_no_muta_matrices_de_entrada(self):
        """La función no debe alterar las matrices originales (pureza)."""
        cargas = [[10, 20], [30, 40]]
        capacidades = [[50, 50], [50, 50]]
        cargas_copia = [fila[:] for fila in cargas]
        capacidades_copia = [fila[:] for fila in capacidades]
        validar_matrices(cargas, capacidades)
        self.assertEqual(cargas, cargas_copia)
        self.assertEqual(capacidades, capacidades_copia)


class TestEsMatrizRegular(unittest.TestCase):

    def test_matriz_regular(self):
        self.assertTrue(es_matriz_regular([[1, 2], [3, 4]]))

    def test_matriz_irregular(self):
        self.assertFalse(es_matriz_regular([[1, 2], [3]]))

    def test_matriz_vacia(self):
        self.assertFalse(es_matriz_regular([]))


if __name__ == "__main__":
    unittest.main()
