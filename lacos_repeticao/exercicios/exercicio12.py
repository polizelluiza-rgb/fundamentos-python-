def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


num = int(input("Digite um número inteiro: "))

if eh_primo(num):
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo.")