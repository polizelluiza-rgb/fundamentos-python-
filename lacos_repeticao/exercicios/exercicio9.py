def contar_pares(inicio, fim):
    quantidade = 0
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            quantidade += 1
    return quantidade

val_inicio = int(input("Digite o número inicial: "))
val_fim = int(input("Digite o número final: "))


total_pares = contar_pares(val_inicio, val_fim)
print(f"A quantidade de números pares entre {val_inicio} e {val_fim} é: {total_pares}")