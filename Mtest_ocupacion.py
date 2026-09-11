"""
Pruebas unitarias del Módulo de Cálculo de Ocupación y Detección de
"""

import unittest
from Mocupacion import calcular_ocupacion


class TestCalcularOcupacion(unittest.TestCase):

    def test_caso_tipico_sin_sobrecarga(self):
        """Cargas por debajo de la capacidad no deben marcarse como sobrecarga."""
        cargas = [[100, 150], [200, 250]]
        capacidades = [[200, 200], [400, 400]]
        resultado = calcular_ocupacion(cargas, capacidades)
        self.assertEqual(resultado["matriz_porcentajes"], [[50.0, 75.0], [50.0, 62.5]])
        self.assertEqual(resultado["celdas_sobrecargadas"], [])

    def test_caso_tipico_con_sobrecarga(self):
        """Celdas que exceden el 100% deben quedar registradas con sus coordenadas."""
        cargas = [[250, 100], [100, 500]]
        capacidades = [[200, 200], [200, 400]]
        resultado = calcular_ocupacion(cargas, capacidades)
        self.assertIn((0, 0), resultado["celdas_sobrecargadas"])
        self.assertIn((1, 1), resultado["celdas_sobrecargadas"])
        self.assertEqual(len(resultado["celdas_sobrecargadas"]), 2)

    def test_borde_exactamente_100_no_es_sobrecarga(self):
        """Una celda exactamente al 100% NO se considera sobrecargada (regla > 100%)."""
        cargas = [[200, 100], [100, 100]]
        capacidades = [[200, 200], [200, 200]]
        resultado = calcular_ocupacion(cargas, capacidades)
        self.assertEqual(resultado["celdas_sobrecargadas"], [])
        self.assertEqual(resultado["matriz_porcentajes"][0][0], 100.0)

    def test_celda_con_carga_cero(self):
        """Una celda con carga en cero debe dar 0.0% de ocupación."""
        cargas = [[0, 100], [50, 50]]
        capacidades = [[200, 200], [200, 200]]
        resultado = calcular_ocupacion(cargas, capacidades)
        self.assertEqual(resultado["matriz_porcentajes"][0][0], 0.0)
        self.assertNotIn((0, 0), resultado["celdas_sobrecargadas"])

    def test_no_muta_matrices_de_entrada(self):
        """La función debe generar una nueva matriz sin alterar las originales."""
        cargas = [[100, 150], [200, 250]]
        capacidades = [[200, 200], [400, 400]]
        cargas_copia = [fila[:] for fila in cargas]
        capacidades_copia = [fila[:] for fila in capacidades]
        calcular_ocupacion(cargas, capacidades)
        self.assertEqual(cargas, cargas_copia)
        self.assertEqual(capacidades, capacidades_copia)

    def test_dimension_minima_2x2(self):
        """Debe funcionar correctamente con el tamaño mínimo permitido 2x2."""
        cargas = [[100, 100], [100, 100]]
        capacidades = [[100, 100], [100, 100]]
        resultado = calcular_ocupacion(cargas, capacidades)
        self.assertEqual(len(resultado["matriz_porcentajes"]), 2)
        self.assertEqual(len(resultado["matriz_porcentajes"][0]), 2)


if __name__ == "__main__":
    unittest.main()
