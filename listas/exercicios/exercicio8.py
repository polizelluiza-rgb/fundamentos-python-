def ordenar_numeros(numeros):

    return sorted(numeros)


numeros_desordenados = [42, 10, 67, 7, 23, 1, 5]

print("Lista original:", numeros_desordenados)

lista_ordenada = ordenar_numeros(numeros_desordenados)

print("Lista em ordem crescente:", lista_ordenada)