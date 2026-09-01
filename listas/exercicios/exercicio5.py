def remover_item(itens, posicao):

    if 0 <= posicao < len(itens):

        item_removido = itens.pop(posicao)
        return item_removido
    else:
        print("Erro: Posição inválida!")
        return None


lista_itens = ["Notebook", "Mouse", "Teclado", "Monitor"]

print("Lista atual de itens:", lista_itens)

posicao_informada = int(input("Digite a posição do item que deseja remover (índice numérico): "))

removido = remover_item(lista_itens, posicao_informada)

if removido is not None:
    print(f"Item removido: {removido}")
    print("Lista atualizada:", lista_itens)