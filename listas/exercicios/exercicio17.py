def vender_produto(estoque, produto):

    if produto in estoque:
        estoque.remove(produto)
        print(f"Venda realizada: '{produto}' foi removido do estoque.")
    else:
        print(f"O produto '{produto}' não está disponível no estoque.")

    return estoque

estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

print("Estoque inicial:", estoque)

produto_venda = input("Digite o nome do produto que deseja vender: ")

estoque_atualizado = vender_produto(estoque, produto_venda)

print("Estoque atualizado:", estoque_atualizado)