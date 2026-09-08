def validar_telefone(numeros):
    if numeros.isdigit():
        return "Número de telefone válido!."
    else:
        return "Número inválido! Digite somente números."

telefone_input = input("Digite o número de telefone: ")

resultado = validar_telefone(telefone_input)
print(resultado)