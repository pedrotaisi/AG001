import sympy as sp

# Definir as variáveis
t = sp.symbols('t')
c = 1991%10

# Definir a equação da velocidade
v = 5*c + 7*t**4 + sp.sqrt(t**3) - 3*c*t**3

# Calcular a equação do deslocamento (integral da velocidade)
s = sp.integrate(v, t)
print("Equação do deslocamento, s(t):")
print(s)

# Calcular o deslocamento de t=1s a t=7s
s_t1 = s.subs(t, 1)
s_t7 = s.subs(t, 7)
deslocamento = s_t7 - s_t1
print("\nDeslocamento de t=1s a t=7s:")
print(deslocamento)

# Calcular a equação da aceleração (derivada da velocidade)
a = sp.diff(v, t)
print("\nEquação da aceleração, a(t):")
print(a)
