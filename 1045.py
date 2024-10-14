# Leitura dos valores de ponto flutuante
A, B, C = map(float, input().split())

# Ordenação dos lados em ordem decrescente
lados = sorted([A, B, C], reverse=True)
A, B, C = lados

# Verificação se formam um triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Cálculo dos quadrados dos lados
    A2 = A**2
    B2 = B**2
    C2 = C**2
    
    # Verificação do tipo de triângulo
    if A2 == B2 + C2:
        print("TRIANGULO RETANGULO")
    elif A2 > B2 + C2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    
    # Verificação de lados iguais
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
