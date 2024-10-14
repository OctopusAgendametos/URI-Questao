# Leitura dos dois valores inteiros
A, B = map(int, input().split())

# Verificação se são múltiplos
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
