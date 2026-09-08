
def substituir_palavra(frase, palavra_1, palavra_2):
    return frase.replace(palavra_1, palavra_2)

frase_usuario = input("Digite uma frase: ")
palavra_antiga = input("Digite a palavra que deseja substituir: ")
palavra_nova = input("Digite a nova palavra: ")

resultado = substituir_palavra(frase_usuario, palavra_antiga, palavra_nova)
print(f"Frase alterada: {resultado}")