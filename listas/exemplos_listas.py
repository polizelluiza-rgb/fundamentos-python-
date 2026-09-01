def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"o nome da lista é {nome}")

lista_de_nomes = ["Luiza", "Camila", "Manu", "Maria", "Jimin"]
mostrar_nomes(lista_de_nomes)

def adicionar_nomes(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nomes(lista_de_nomes, "Niki")

def adicionar_nome_posiçao(nomes, nome, posicao):
    nomes.insert(posicao,nome)
    print(f'o {nome} foi inserido na posoçao {posicao} da lista: {nomes}')

adicionar_nome_posiçao(lista_de_nomes, "Luiza", posicao=2)


def juntar_nomes(nomes,novos_nomes):
    nomes.extend(novos_nomes)
    print(f'o {novos_nomes} foi inserido {nomes}')

novos_nomes = ["Evan", "Jake"]

juntar_nomes(lista_de_nomes, novos_nomes)


def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print('Este nome nao existe na lista')

    nomes.remove(nome)
    print(f'o {nome} foi removido na lista: {nomes}')

remover_nome_pelo_valor(lista_de_nomes, "Luiza")


def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f'o nome da posicao {posicao} é {nomes[posicao]}, foi removido')
    remover_nome_pelo_indice(lista_de_nomes, posicao=2 )


def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print('Este nome nao existe na lista')
    posicao = nomes.index(nome)
    print(f'a posicao do nome {nome} é {posicao}')

encontrar_posicao_pelo_valor(lista_de_nomes, "Evan")


def quantidade_de_nomes(nomes):

    quantidade = len(nomes)
    print(f'Quantidade de nomes da lista {quantidade}')

quantidade_de_nomes(lista_de_nomes)

def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f'a lista ordenada é {lista_de_nomes_ordenados}')

ordenar_nomes(lista_de_nomes)


def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)

    media = (total / quantidade)
    print(f'a media das notas é {media}')

notas_semestre = [7.8, 6.5, 9, 9.5, 10]

calcular_media(notas_semestre)


def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)

    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)
    return ordenadas, media

notas_ordenadas, niki = gerenciar_notas(notas_semestre, nova_nota=7)
print(f'notas ordenadas = {notas_ordenadas}')
print(f'a media das notas é {niki}')







































