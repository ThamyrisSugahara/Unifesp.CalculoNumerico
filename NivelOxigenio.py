import math

# Define a função f(x) que queremos que seja zero (C(x) - 5 = 0)
def f(x):
    return 5 - 20 * (math.exp(-0.2 * x) - math.exp(-0.75 * x))

# Define a derivada de f(x)
def f_prime(x):
    return 4 * math.exp(-0.2 * x) - 15 * math.exp(-0.75 * x)

# Método de Newton-Raphson
def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)

        # Evita divisão por zero
        if fpx == 0:
            print("Derivada zero, método falhou.")
            return None

        # Calcula o próximo valor de x usando Newton-Raphson
        x_new = x - fx / fpx

        # Verifica se a diferença entre x_new e x é menor que a tolerância
        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    print("O método não convergiu após o número máximo de iterações.")
    return None


# Chute inicial para x
initial_guess = 1 # Aproximação inicial próxima da solução esperada
x_solution = newton_raphson(initial_guess)

if x_solution is not None:
    print(f"A distância para a qual o nível de oxigênio desce para 5 é aproximadamente: {x_solution}")
