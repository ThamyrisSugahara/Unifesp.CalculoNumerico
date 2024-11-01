import numpy as np

# Definindo os valores conhecidos
h = 290
C = 1100
F = 0.7
D = 13

# Função com a fórmula de Vant-Hull (1976)
def func(A):
    num = np.pi * ((h / np.cos(A)) ** 2) * F
    den = 0.5 * np.pi * (D ** 2) * (1 + np.sin(A) - 0.5 * np.cos(A))
    return num / den - C
def secant_method(x0, x1, tolerance=1e-6, max_iterations=100):
    for iteration in range(max_iterations):
        f_x0 = func(x0)
        f_x1 = func(x1)

        # Mostra a iteração atual e o valor de A
        print(f"Iteração {iteration + 1}: A = {np.degrees(x1):.6f} graus, func(A) = {f_x1:.6f}")

        if abs(f_x1) < tolerance:
            print(f"\nO valor de A em graus é: {np.degrees(x1):.6f}")
            return np.degrees(x1)

        # Calcula o próximo ponto usando a fórmula da secante
        try:
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        except ZeroDivisionError:
            print("Divisão por zero na fórmula da secante. O método falhou.")
            return None

        x0, x1 = x1, x2  # Atualiza os pontos

    print("O método da Secante não convergiu dentro do número máximo de iterações.")
    return None

# Estimativa inicial
x0 = np.radians(30)  # Aproximação inicial em radianos
x1 = np.radians(60)  # Segunda aproximação inicial em radianos

# Chamada do método
secant_method(x0, x1)
