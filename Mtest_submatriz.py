"""
Pruebas unitarias del Módulo de Extracción de Submatriz de Sobrecarga
"""

import unittest
from Msubmatriz import extraer_submatriz_critica


class TestExtraerSubmatrizCritica(unittest.TestCase):

    def test_caso_tipico_criterio_promedio(self):
        matriz = [
            [50, 60, 200, 210],
            [40, 30, 190, 220],
            [10, 20, 30, 40],
        ]
        resultado = extraer_submatriz_critica(matriz, k=2, p=2, criterio="promedio")
        self.assertEqual(resultado["posicion"], (0, 2))
        self.assertEqual(resultado["submatriz"], [[200, 210], [190, 220]])

    def test_criterio_conteo_sobrecarga(self):
        matriz = [
            [50, 60, 105, 110],
            [40, 30, 90, 120],
        ]
        resultado = extraer_submatriz_critica(
            matriz, k=2, p=2, criterio="conteo_sobrecarga"
        )
        self.assertEqual(resultado["posicion"], (0, 2))

    def test_ventana_igual_a_toda_la_matriz(self):
        """Cuando k x p coincide exactamente con N x M, solo existe una ventana."""
        matriz = [[10, 20], [30, 40]]
        resultado = extraer_submatriz_critica(matriz, k=2, p=2)
        self.assertEqual(resultado["submatriz"], matriz)
        self.assertEqual(resultado["posicion"], (0, 0))

    def test_ventana_1x1_devuelve_celda_maxima(self):
        matriz = [[10, 999], [30, 40]]
        resultado = extraer_submatriz_critica(matriz, k=1, p=1)
        self.assertEqual(resultado["submatriz"], [[999]])
        self.assertEqual(resultado["posicion"], (0, 1))

    def test_ventana_mayor_a_la_matriz_lanza_error(self):
        matriz = [[10, 20], [30, 40]]
        with self.assertRaises(ValueError):
            extraer_submatriz_critica(matriz, k=3, p=2)

    def test_dimensiones_invalidas_lanza_error(self):
        matriz = [[10, 20], [30, 40]]
        with self.assertRaises(ValueError):
            extraer_submatriz_critica(matriz, k=0, p=1)
        with self.assertRaises(ValueError):
            extraer_submatriz_critica(matriz, k=1, p=-1)

    def test_no_muta_matriz_de_entrada(self):
        matriz = [[10, 20, 30], [40, 50, 60]]
        matriz_copia = [fila[:] for fila in matriz]
        extraer_submatriz_critica(matriz, k=2, p=2)
        self.assertEqual(matriz, matriz_copia)


if __name__ == "__main__":
    unittest.main()
