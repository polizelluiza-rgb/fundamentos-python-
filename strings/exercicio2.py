def nome_minusculo(nome):
    return nome.lower()

nome_usuario = input("Digite o seu nome: ")

resultado = nome_minusculo(nome_usuario)
print(f"Nome em minúsculas: {resultado}")