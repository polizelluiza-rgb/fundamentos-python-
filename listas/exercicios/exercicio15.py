def adicionar_produtos(compras, produtos):

    compras.extend(produtos)
    print("Produtos adicionados à lista de compras!")

def cancelar_compra(compras, produto):

    if produto in compras:
        compras.remove(produto)
        print(f"O produto '{produto}' foi cancelado e removido da lista.")
    else:
        print(f"O produto '{produto}' não foi encontrado na lista de compras.")

lista_compras = ["Maçã", "Pão", "Leite"]
novos_produtos = ["Arroz", "Feijão", "Café"]

print("Lista de compras inicial:", lista_compras)
print("Novos produtos para adicionar:", novos_produtos)

adicionar_produtos(lista_compras, novos_produtos)
print("Lista de compras atualizada:", lista_compras)

print("\n--- Cancelamento de Produto ---")
produto_cancelar = input("Digite o nome do produto que deseja cancelar: ")

cancelar_compra(lista_compras, produto_cancelar)
print("Lista de compras final:", lista_compras)