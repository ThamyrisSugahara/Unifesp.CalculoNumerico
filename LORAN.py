import numpy as np

# Parâmetros
c = 300_000  # Velocidade do sinal em km/s
tAB = 0.0001  # Diferença de tempo entre A e B em segundos
tAC = 0.00015  # Diferença de tempo entre A e C em segundos

# Coordenadas das estações
xA, yA = 0, 0
xB, yB = 100, 0
xC, yC = 50, 100


# Funções do sistema não linear
def f(x, y):
    return np.array([
        np.sqrt((x - xB) ** 2 + (y - yB) ** 2) - np.sqrt(x ** 2 + y ** 2) - c * tAB,
        np.sqrt((x - xC) ** 2 + (y - yC) ** 2) - np.sqrt(x ** 2 + y ** 2) - c * tAC
    ])


# Jacobiana do sistema
def jacobian(x, y):
    rA = np.sqrt(x ** 2 + y ** 2)
    rB = np.sqrt((x - xB) ** 2 + (y - yB) ** 2)
    rC = np.sqrt((x - xC) ** 2 + (y - yC) ** 2)

    return np.array([
        [(x - xB) / rB - x / rA, (y - yB) / rB - y / rA],
        [(x - xC) / rC - x / rA, (y - yC) / rC - y / rA]
    ])


# Método de Newton
def newton_method(f, jacobian, x0, y0, tol=1e-6, max_iter=100):
    x, y = x0, y0
    for i in range(max_iter):
        # Calcula o valor das funções e da Jacobiana
        F = f(x, y)
        J = jacobian(x, y)

        # Atualiza as variáveis usando o Método de Newton
        delta = np.linalg.solve(J, -F)
        x, y = x + delta[0], y + delta[1]

        # Verifica a convergência
        if np.linalg.norm(delta) < tol:
            return x, y, i + 1
    raise ValueError("O método não convergiu após o número máximo de iterações")


# Aproximação inicial
x0, y0 = 50, 50

# Resolve o sistema
try:
    x_sol, y_sol, iterations = newton_method(f, jacobian, x0, y0)
    print(f"Posição estimada do receptor: x = {x_sol:.6f}, y = {y_sol:.6f}")
    print(f"Número de iterações: {iterations}")
except ValueError as e:
    print(e)
