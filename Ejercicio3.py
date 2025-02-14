# Importar las bibliotecas necesarias
import numpy as np               # Para cálculos numéricos y manejo de arrays
import matplotlib.pyplot as plt  # Para graficar los resultados

# Definir la función g(x) para el método de punto fijo
# En este caso, g(x) está definida como g(x) = cos(x)
# Esta elección se basa en reorganizar una ecuación no lineal para aplicar el método de punto fijo
def g(x):
    return np.cos(x)

# Derivada de g(x) para analizar la convergencia
# La convergencia del método de punto fijo depende de que el valor absoluto de g'(x) sea menor que 1
# Esto garantiza que las iteraciones se acerquen al punto fijo
def g_prime(x):
    return -np.sin(x)

# Función para calcular el error absoluto entre dos iteraciones consecutivas
# Esto se utiliza como criterio de convergencia para detener el método
# x_new: Valor actual de la iteración
# x_old: Valor de la iteración anterior
def error_absoluto(x_new, x_old):
    return abs(x_new - x_old)

# Implementación del Método de Punto Fijo
# Este método se utiliza para encontrar soluciones a ecuaciones no lineales
# al reorganizarlas en una forma g(x) = x.
# Parámetros:
#   x0: Valor inicial de la iteración
#   tol: Tolerancia para el criterio de convergencia (por defecto 1e-5)
#   max_iter: Máximo número de iteraciones permitidas (por defecto 100)
def punto_fijo(x0, tol=1e-5, max_iter=100):
    # Listas para almacenar los resultados de cada iteración
    iteraciones = []  # Para guardar el número de iteración, valor de x y error absoluto
    errores_abs = []  # Para guardar los errores absolutos

    # Inicializar el valor anterior con el valor inicial dado
    x_old = x0

    # Bucle de iteraciones del método de punto fijo
    for i in range(max_iter):
        # Calcular el nuevo valor aplicando la función g(x)
        x_new = g(x_old)

        # Calcular el error absoluto
        e_abs = error_absoluto(x_new, x_old)

        # Guardar los resultados de la iteración actual
        iteraciones.append((i+1, x_new, e_abs))
        errores_abs.append(e_abs)

        # Verificar el criterio de convergencia
        # Si el error absoluto es menor que la tolerancia, detener las iteraciones
        if e_abs < tol:
            break

        # Actualizar el valor anterior para la siguiente iteración
        x_old = x_new

    # Devolver todas las iteraciones y los errores absolutos para análisis posterior
    return iteraciones, errores_abs

# Parámetro inicial para el método de punto fijo
x0 = 0.5  # Valor de inicio

# Ejecutar el método de punto fijo y guardar los resultados
iteraciones, errores_abs = punto_fijo(x0)

# Imprimir una tabla con los resultados de cada iteración
print("Iteración | x_n      | Error absoluto")
print("-------------------------------------")
for it in iteraciones:
    print(f"{it[0]:9d} | {it[1]:.6f} | {it[2]:.6e}")

# Graficar la función g(x) junto con la línea y=x para visualizar la convergencia
# Rango de valores para x
x_vals = np.linspace(-1, 1, 100)
y_vals = g(x_vals)

# Configurar el tamaño de la gráfica
plt.figure(figsize=(8, 5))

# Graficar la función g(x)
plt.plot(x_vals, y_vals, label=r"$g(x) = \cos(x)$", color="blue")

# Graficar la línea y=x para ver los puntos de intersección (soluciones fijas)
plt.plot(x_vals, x_vals, linestyle="dashed", color="red", label="y = x")

# Graficar los puntos de las iteraciones en el diagrama
x_points = [it[1] for it in iteraciones]  # Valores de x de las iteraciones
y_points = [g(x) for x in x_points]       # Valores de g(x) correspondientes
plt.scatter(x_points, y_points, color="black", zorder=3)
plt.plot(x_points, y_points, linestyle="dotted", color="black", label="Iteraciones")

# Etiquetas y título del gráfico
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.title("Método de Punto Fijo")
plt.show()

# Graficar la evolución del error absoluto en función del número de iteraciones
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(errores_abs) + 1), errores_abs, marker="o", label="Error absoluto")

# Etiquetas y título del gráfico
plt.xlabel("Iteración")
plt.ylabel("Error absoluto")
plt.yscale("log")  # Escala logarítmica para visualizar mejor la convergencia
plt.legend()
plt.grid(True)
plt.title("Evolución del Error Absoluto")
plt.show()
