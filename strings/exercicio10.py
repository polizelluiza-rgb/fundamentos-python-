def separar_nome(nome_completo):
    partes = nome_completo.split()
    for parte in partes:
        print(parte)

nome_usuario = input("Digite o nome completo: ")

separar_nome(nome_usuario)