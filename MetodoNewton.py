# Definindo a função f(x) e sua derivada f'(x)
def f(x: float) -> float:
    return x**5 - 3*x**3 - 5*x + 4

def f_prime(x: float) -> float:
    return 5*x**4 - 9*x**2 - 5

# Método de Newton
def newton_method(x0: float, tol: float = 1e-6, max_iter: int = 100) -> tuple[float, int]:
    xk = x0
    for i in range(max_iter):
        fxk = f(xk)
        if abs(fxk) < tol:  # Critério de parada
            return xk, i
        fpxk = f_prime(xk)
        if fpxk == 0:  # Evitar divisão por zero
            print("Derivada zero, não é possível continuar.")
            return None, i

        # Imprimindo a raiz em cada iteração
        print(f"Iteração {i + 1}: x = {xk}")

        xk = xk - fxk / fpxk
    return xk, max_iter

# Definindo x0
x0 = 1

# Chamando o método de Newton
root, iterations = newton_method(x0)

# Imprimindo os resultados
print(f"A raiz encontrada é: {root}")
print(f"Quantidade de iterações: {iterations}")
