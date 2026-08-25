def validar_senha(senha_correta):
    tentativas = 3

    while tentativas > 0:
        senha_digitada = input("Digite a senha: ")

        if senha_digitada == senha_correta:
            print("Acesso permitido!")
            return True
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")
            else:
                print("Acesso bloqueado! Você excedeu o número de tentativas.")
                return False



senha_cadastrada = "python123"
validar_senha(senha_cadastrada)