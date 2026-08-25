def mostrar_multiplos(numero):
    for i in range(1, 11):
        print(numero * i)


num = int(input("Digite um número para ver seus 10 primeiros múltiplos: "))

mostrar_multiplos(num)