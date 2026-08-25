def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def mostrar_primos(inicio, fim):
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            print(num)

val_inicio = int(input("Digite o número inicial do intervalo: "))
val_fim = int(input("Digite o número final do intervalo: "))

print(f"Números primos entre {val_inicio} e {val_fim}:")
mostrar_primos(val_inicio, val_fim)