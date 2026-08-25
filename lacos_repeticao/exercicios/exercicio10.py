def somar_pares(inicio, fim):
    soma = 0
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma += i
    return soma


val_inicio = int(input("Digite o número inicial: "))
val_fim = int(input("Digite o número final: "))

resultado = somar_pares(val_inicio, val_fim)
print(f"A soma de todos os números pares entre {val_inicio} e {val_fim} é: {resultado}")