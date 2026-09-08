def nome_maiusculo(nome):
    return nome.upper()

nome_usuario = input("Digite o seu nome: ")

resultado = nome_maiusculo(nome_usuario)
print(f"Nome em maiúsculas: {resultado}")