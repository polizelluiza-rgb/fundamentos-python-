def verificar_palavra(texto, palavra):
    if palavra in texto:
        return "Palavra encontrada!"
    else:
        return "Palavra não encontrada!"

texto_usuario = input("Digite o texto: ")
palavra_usuario = input("Digite a palavra que deseja verificar: ")

resultado = verificar_palavra(texto_usuario, palavra_usuario)
print(resultado)