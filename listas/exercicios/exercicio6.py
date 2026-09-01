def encontrar_produto(produtos, produto):

    if produto in produtos:
        posicao = produtos.index(produto)
        return posicao
    else:
        print(f"O produto '{produto}' não foi encontrado na lista.")
        return -1


lista_produtos = ["Notebook", "Celular", "Fone de Ouvido", "Carregador"]

print("Lista de produtos disponíveis:", lista_produtos)

produto_procurado = input("Digite o nome do produto que deseja procurar: ")

posicao_encontrada = encontrar_produto(lista_produtos, produto_procurado)

if posicao_encontrada != -1:
    print(f"O produto '{produto_procurado}' foi encontrado na posição (índice): {posicao_encontrada}")