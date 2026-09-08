def criar_email(nome, sobrenome, dominio):
    email = nome.lower() + "." + sobrenome.lower() + "@" + dominio.lower()
    return email

nome_input = input("Digite o nome: ")
sobrenome_input = input("Digite o sobrenome: ")
dominio_input = input("Digite o domínio (ex: exemplo.com): ")

resultado = criar_email(nome_input, sobrenome_input, dominio_input)
print(f"E-mail gerado: {resultado}")