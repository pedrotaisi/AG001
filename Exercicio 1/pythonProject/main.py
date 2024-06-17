import sympy as sp

n = 1991%10 + 1

# Questão 1
x = sp.symbols('x')
f = (2*(x*x) - 7)/ (7*(pow(x,5) - 2))
limite = sp.limit(f, x, 1)

print("O resultado é: ")
print(limite*n)
print("\n")


# Questão 2
x = sp.symbols('x')
f = (2*(x*x) - 7)/ (7*(pow(x,5) - 2))
limite = sp.limit(f, x, sp.oo)

print("O resultado é: ")
print(limite*n)
print("\n")


# Questão 3
x = sp.symbols('x')
f = (2*(x*x) - 7)/ (7*(pow(x,5) - 2))
limite = sp.limit(f, x, -sp.oo)

print("O resultado é: ")
print(limite*n)
print("\n")


