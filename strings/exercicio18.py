def validar_senha(senha):
    if len(senha) < 8:
        return "Senha inválida!"

    tem_letra = False
    tem_numero = False

    for caractere in senha:
        if caractere.isspace():
            return "Senha inválida!"
        if caractere.isalpha():
            tem_letra = True
        if caractere.isdigit():
            tem_numero = True

    if tem_letra and tem_numero:
        return "Senha válida!"
    else:
        return "Senha inválida!"


senha_input = input("Digite a senha a ser validada: ")

resultado = validar_senha(senha_input)
print(f"Resultado: {resultado}")