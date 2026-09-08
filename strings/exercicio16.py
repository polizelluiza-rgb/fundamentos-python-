def verificar_extensao(nome_arquivo):
    if nome_arquivo.endswith(".pdf"):
        return "Arquivo válido."
    else:
        return "Arquivo inválido."

arquivo_input = input("Digite o nome do arquivo com a extensão: ")

resultado = verificar_extensao(arquivo_input)
print(resultado)