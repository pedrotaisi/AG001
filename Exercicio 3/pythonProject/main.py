import sympy as sp

# Definir a variável
x = sp.symbols('x')

# Definir a constante c
c = 1991%10

# Definir a equação da força com c substituído por 1
F = 5*x**3 + sp.sqrt(x**3/35) + (3/4)*x - 3*c

# Calcular o trabalho (integral da força entre x=3 e x=8)
trabalho = sp.integrate(F, (x, 3, 8))
print(trabalho)
