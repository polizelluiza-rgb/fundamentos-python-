def trocar_valores():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    print("\nAntes:")
    print(f"A = {a}")
    print(f"B = {b}")

    a, b = b, a

    print("\nDepois:")
    print(f"A = {a}")
    print(f"B = {b}")


trocar_valores()