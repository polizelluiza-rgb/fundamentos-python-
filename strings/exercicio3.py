def formatar_nome(nome):
    return nome.title()

nome_usuario = input("Digite o seu nome: ")

resultado = formatar_nome(nome_usuario)
print(f"Nome formatado: {resultado}")