# das172-examen2-Hernandez-Diego
Examen Práctico Unidad II
Auditoría y Balance Matricial de Distribución de Carga en Bahía de Aeronave

Proyecto desarrollado para la asignatura Desarrollo de Algoritmos para la Simulación de Sistemas en la Universidad Don Bosco, Facultad de Aeronáutica, Escuela de Ingeniería Aeronáutica.

1. Explicación del Problema
En el transporte aéreo de carga, la forma en la que se distribuye el peso dentro de la bodega de una aeronave es clave para la seguridad. Básicamente hay que cuidar dos cosas principales: que el piso de la bodega no sufra daños estructurales por pasarse del límite en una sola celda, y que el peso esté bien balanceado entre los lados izquierdo y derecho (babor y estribor) para no afectar el centro de gravedad del avión durante el vuelo.

Para resolver esto, modelamos la bodega como una matriz de tamaño N por M. Usando dos matrices de entrada —las cargas reales y las capacidades máximas permitidas— el programa se encarga de validar que las dimensiones sean correctas, calcular los porcentajes de ocupación celda por celda, revisar el balance lateral y encontrar la zona de la bodega con mayor concentración de sobrecarga mediante una ventana de búsqueda.

2. Arquitectura y Funcionamiento
El código está dividido en varios módulos independientes para mantener todo ordenado y sin mezclar lógica. Cada archivo recibe sus datos por parámetros y devuelve estructuras nuevas sin alterar las matrices originales.

El flujo principal corre desde el archivo main.py, que primero llama a las validaciones de dimensiones y rangos. Si todo sale bien, pasa al cálculo de ocupación y al análisis de balance lateral. Por último, toma esa información para extraer la submatriz crítica con el algoritmo de ventana deslizante. Como no hay variables globales, cada parte se puede probar por separado de forma bien sencilla.

3. Complejidad Computacional
El tiempo de ejecución del sistema se mantiene en un orden de O(N x M). Esto pasa porque las funciones recorren las celdas de las matrices de forma lineal para validar, sacar porcentajes o sumar los pesos laterales. La parte de la búsqueda de la submatriz crítica también se comporta de manera eficiente porque el tamaño de la ventana (k por p) es un valor acotado y definido por el usuario, evitando que el proceso se vuelva pesado. En cuanto a la memoria, se consumen recursos de forma proporcional al tamaño de las matrices sin duplicar datos innecesariamente.

4. Estructura del Repositorio
Como el proyecto utiliza una estructura de archivos plana directamente en la raíz, los componentes se distribuyen de la siguiente manera:

Mvalidacion.py: Revisa que las matrices sean regulares, tengan un tamaño mínimo de 2x2 y contengan valores de peso y capacidad válidos.

Mbalance.py: Calcula los pesos totales por cada fila longitudinal y mide el desbalance lateral entre las mitades de la bodega.

Mocupacion.py: Saca los porcentajes de ocupación de cada celda y marca las que superan el 100%.

Msubmatriz.py: Aplica la ventana deslizante para encontrar la zona más crítica de sobrecarga.

main.py: Script principal que junta todos los módulos y muestra una ejecución de prueba completa.

Mtest_validacion.py, Mtest_balance.py, Mtest_ocupacion.py, Mtest_submatriz.py: Archivos individuales con las pruebas unitarias usando unittest.

README.md y .gitignore.

5. Cómo Ejecutar el Proyecto
Solo necesitas tener instalado Python 3. Para ver la simulación y el flujo completo funcionando, ejecutas en tu terminal:
python main.py

Y si quieres correr las pruebas unitarias de cada módulo por separado, puedes hacerlo con comandos como estos:

python -m unittest Mtest_validacion.py
python -m unittest Mtest_balance.py
python -m unittest Mtest_ocupacion.py
python -m unittest Mtest_submatriz.py
