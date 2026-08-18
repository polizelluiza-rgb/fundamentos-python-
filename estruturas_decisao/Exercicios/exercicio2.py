def par_ou_impar():
    entrada = input("Digite um número inteiro: ")
    numero = int(entrada)

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    elif numero % 2 != 0:
        print(f"O número {numero} é impar.")
    else:
        print("numero inválido.")

par_ou_impar()