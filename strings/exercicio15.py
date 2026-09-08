def validar_especie(animal):
    if animal.isalpha():
        return "Espécie de animal válida."
    else:
        return "Espécie inválida."

especie_input = input("Digite a espécie do animal: ")

resultado = validar_especie(especie_input)
print(resultado)