def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

num = int(input("Digite um número para calcular o fatorial: "))

if num < 0:
    print("Não existe fatorial de número negativo.")
else:
    res = fatorial(num)
    print(f"O fatorial de {num}! é: {res}")