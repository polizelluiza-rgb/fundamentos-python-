def adicionar_convidados(convidados, novos_convidados):

    convidados.extend(novos_convidados)

    print("Lista final de convidados:", convidados)


lista_convidados = ["Sunoo", "Jungwon"]

quantidade = int(input("Quantos novos convidados deseja adicionar? "))
novos = []

for i in range(quantidade):
    nome = input(f"Digite o nome do novo convidado {i + 1}: ")
    novos.append(nome)

adicionar_convidados(lista_convidados, novos)