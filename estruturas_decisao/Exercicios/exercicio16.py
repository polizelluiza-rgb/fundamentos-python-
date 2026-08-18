def siatema_de_login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario != "admin":
        print("Usuário não encontrado")
    elif senha != "1234":
        print("Senha incorreta")
    else:
        print("Login realizado com sucesso")


siatema_de_login()