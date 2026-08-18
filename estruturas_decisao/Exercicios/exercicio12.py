def verificaçao_de_senha():
        senha_correta = "python123"

        while True:
            senha_digitada = input("Digite a senha: ")

            if senha_digitada == senha_correta:
                print("Acesso permitido")
                break
            else:
                print("Senha inválida")


verificaçao_de_senha()