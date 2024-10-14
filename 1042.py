# Leitura dos três valores inteiros
valores = list(map(int, input().split()))

# Cópia dos valores para manter a ordem original
valores_originais = valores.copy()

# Ordenação dos valores
valores.sort()

# Impressão dos valores em ordem crescente
for valor in valores:
    print(valor)

# Linha em branco
print()

# Impressão dos valores na ordem original
for valor in valores_originais:
    print(valor)
