# Leitura das notas
N1, N2, N3, N4 = map(float, input().split())

# Cálculo da média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / (2 + 3 + 4 + 1)

# Saída da média
print(f"Media: {media:.1f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Leitura da nota do exame
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Cálculo da nova média
    media_final = (media + nota_exame) / 2
    
    # Verificação da situação final do aluno
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    # Saída da média final
    print(f"Media final: {media_final:.1f}")
