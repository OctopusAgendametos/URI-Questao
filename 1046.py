# Leitura das horas de início e fim
hora_inicial, hora_final = map(int, input().split())

# Cálculo da duração
if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = 24 - hora_inicial + hora_final

# Imprime o resultado
print(f"O JOGO DUROU {duracao} HORA(S)")
