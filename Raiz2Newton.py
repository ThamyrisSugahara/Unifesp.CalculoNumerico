import math
def newton_method(x0, tol):
    iterations = 0
    x_n = x0
    while True:
        x_n1 = x_n - (x_n**2 - 2) / (2 * x_n)  # Fórmula de Newton para f(x) = x^2 - 2
        if abs(x_n1 - x_n) < tol:  # Critério de parada com erro absoluto
            return x_n1, iterations
        x_n = x_n1
        iterations += 1

# Definindo a precisão para o método de Newton
tolerance = 1e-6

true_value = math.sqrt(2)

# Comparando o número de iterações para obtenção de uma aproximação com o mesmo erro e precisão
newton_result_1, newton_iterations_1 = newton_method(1, tolerance)
newton_result_2, newton_iterations_2 = newton_method(2, tolerance)

newton_error_1 = abs(newton_result_1 - true_value)
newton_error_2 = abs(newton_result_2 - true_value)

# Resultados do método de Newton
print((newton_result_1, newton_iterations_1, newton_error_1))
print((newton_result_2, newton_iterations_2, newton_error_2))
