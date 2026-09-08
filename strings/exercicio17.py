def limpar_telefone(telefone):
    telefone_limpo = telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    return telefone_limpo

telefone_input = input("Digite o telefone no formato (19) 99999-8888: ")


resultado = limpar_telefone(telefone_input)
print(resultado)