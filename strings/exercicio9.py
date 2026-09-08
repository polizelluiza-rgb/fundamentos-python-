def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

texto_usuario = input("Digite um texto: ")

quantidade = contar_palavras(texto_usuario)
print(f"O texto contém {quantidade} palavra(s).")