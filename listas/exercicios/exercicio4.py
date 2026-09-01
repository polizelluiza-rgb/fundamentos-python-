def remover_produto(produtos, produto):

    if produto in produtos:
        produtos.remove(produto)
        print(f"Produto '{produto}' removido com sucesso!")
        print("Lista de produtos atualizada:", produtos)
    else:
        print(f"O produto '{produto}' não foi encontrado na lista.")


lista_produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]

print("Lista atual de produtos:", lista_produtos)

produto_para_remover = input("Digite o nome do produto que deseja remover: ")


remover_produto(lista_produtos, produto_para_remover)