def inverter_lista(lista):

    lista_invertida = list(reversed(lista))
    return lista_invertida

lista_exemplo = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

print("Lista original:", lista_exemplo)

resultado = inverter_lista(lista_exemplo)


print("Lista invertida:", resultado)