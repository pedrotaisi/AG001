import math

#Equação 1
def equacao(x, c):
    return math.exp(x - 3) + math.exp(x - 1) + math.exp(x) - (c + 1)

def derivada(x):
    return math.exp(x - 3) + math.exp(x - 1) + math.exp(x)

def newton_raphson(c, tolerancia=1e-6, max_iter=100, x0=0):
    xn = x0
    for i in range(max_iter):
        f_xn = equacao(xn, c)
        f_derivada_xn = derivada(xn)
        xn_next = xn - f_xn / f_derivada_xn
        if abs(xn_next - xn) < tolerancia:
            return xn_next
        xn = xn_next
    return None

c = 1  # valor de c
x0 = 0  # valor inicial de x
raiz = newton_raphson(c, x0 = x0)

if raiz is not None:
    print("A solução para a equação é:", raiz)
else:
    print("Não foi possível encontrar uma solução dentro do limite de iterações.")

#Equação 2
def equacao(x, c):
    return x**4 - 4*x**3 + 3*x - c

def bissecao(c, a, b, tolerancia=1e-6, max_iter=100):
    fa = equacao(a, c)
    fb = equacao(b, c)

    if fa * fb > 0:
        print("Intervalo inválido.")
        return None

    for i in range(max_iter):
        xn = (a + b) / 2
        fn = equacao(xn, c)

        if abs(fn) < tolerancia:
            return xn
        elif fa * fn < 0:
            b = xn
        else:
            a = xn

    print("O método da bisseção não convergiu.")
    return None

c = 1  # valor de c
a = -10
b = 10

raiz = bissecao(c, a, b)

if raiz is not None:
    print("A solução para a equação é:", raiz)
else:
    print("Não foi possível encontrar uma solução dentro do limite de iterações.")


#Equação 3

import math

def equacao(x, c):
    return 4 * math.sin((c + 1) * x) + 2

def bissecao(c, a, b, tolerancia=1e-6, max_iter=100):
    fa = equacao(a, c)
    fb = equacao(b, c)

    if fa * fb > 0:
        print("Intervalo inválido.")
        return None

    for i in range(max_iter):
        xn = (a + b) / 2
        fn = equacao(xn, c)

        if abs(fn) < tolerancia:
            return xn
        elif fa * fn < 0:
            b = xn
        else:
            a = xn

    print("O método da bisseção não convergiu.")
    return None

c = 1  # valor de c
a = -10
b = 10

raiz = bissecao(c, a, b)

if raiz is not None:
    print("A solução para a equação é:", raiz)
else:
    print("Não foi possível encontrar uma solução dentro do limite de iterações.")


