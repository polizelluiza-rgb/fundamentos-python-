def maior_numero():
    maior = None

    while True:
        numero = float(input("Digite um número: "))

        if maior is None or numero > maior:
            maior = numero

        continuar = input("Deseja inserir outro número? (s/n): ").strip().lower()
        if continuar != 's':
            break

    return maior


resultado = maior_numero()

if resultado is not None:
    print(f"O maior número digitado foi: {resultado}")