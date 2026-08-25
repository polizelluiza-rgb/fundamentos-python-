def mostrar_impares(numero):
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i)

limite = int(input("Digite um número inteiro: "))
mostrar_impares(limite)