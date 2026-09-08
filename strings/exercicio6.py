def contar_letra(frase, letra):
    return frase.count(letra)

frase_usuario = input("Digite uma frase: ")
letra_usuario = input("Digite a letra que deseja contar: ")

resultado = contar_letra(frase_usuario, letra_usuario)
print(f"A letra '{letra_usuario}' aparece {resultado} vez(es) na frase.")