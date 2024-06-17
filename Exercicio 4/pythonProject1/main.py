import numpy as np

# Valores dos resistores e das fontes de tensão
R1 = 15000
R2 = 5000
R3 = 10000
V1 = 7 + (5*(1991%10))
V2 = 4 + (2*(1991%10))
V3 = 3 + (4*(1991%10))

# Coeficientes das equações
A = np.array([
    [R1, R3],
    [R3, R2]
])

# Vetor de tensões
B = np.array([
    V1 - V2,
    V2 - V3
])

# Resolvendo o sistema de equações lineares
currents = np.linalg.solve(A, B)
I1, I2 = currents

print(f"A corrente I1 na malha M1 é: {I1} A")
print(f"A corrente I2 na malha M2 é: {I2} A")
