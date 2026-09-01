def adicionar_nome(nomes, nome):

    nomes.append(nome)


    print("Lista de nomes atualizada:", nomes)

lista_de_nomes = ["Niki", "Sunghoon", "Jake"]

novo_nome = input("Digite o nome que deseja adicionar: ")

adicionar_nome(lista_de_nomes, novo_nome)