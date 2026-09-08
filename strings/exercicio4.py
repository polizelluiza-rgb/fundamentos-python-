def limpar_texto(texto):
    return texto.strip()

texto_usuario = input("Digite um texto com espaços no início e/ou no final: ")

resultado = limpar_texto(texto_usuario)
print(f"Texto limpo: '{resultado}'")