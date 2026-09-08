def procurar_palavra(texto, palavra):
    posicao = texto.find(palavra)

    if posicao != -1:
        return f"A palavra '{palavra}' começa na posição {posicao}."
    else:
        return f"A palavra '{palavra}' não existe no texto."


texto_usuario = input("Digite o texto: ")
palavra_usuario = input("Digite a palavra que deseja procurar: ")


resultado = procurar_palavra(texto_usuario, palavra_usuario)
print(resultado)