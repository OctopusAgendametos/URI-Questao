# Leitura dos valores A, B e C
A, B, C = map(float, input().split())

# Verificação se formam um triângulo
if A + B > C and A + C > B and B + C > A:
    # Cálculo do perímetro
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Cálculo da área do trapézio
    area = (A + B) * C / 2
    print(f"Area = {area:.1f}")
