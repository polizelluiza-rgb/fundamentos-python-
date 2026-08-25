def somar_ate(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

num = int(input("Digite um número inteiro: "))

resultado = somar_ate(num)
print(f"A soma de todos os números de 1 até {num} é: {resultado}")