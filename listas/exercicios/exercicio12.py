def calcular_media(notas):

    total = sum(notas)

    quantidade = len(notas)

    media = total / quantidade
    return media

lista_notas = [8.5, 7.0, 9.5, 6.0]

print("Notas informadas:", lista_notas)

resultado_media = calcular_media(lista_notas)

print(f"A média das notas é: {resultado_media:.2f}")