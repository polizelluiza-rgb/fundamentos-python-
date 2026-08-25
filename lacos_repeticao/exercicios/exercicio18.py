def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]
    print(f"\nNotas para o valor de R$ {valor}:")

    for nota in notas:
        qtd_notas = valor // nota
        if qtd_notas > 0:
            print(f"{qtd_notas} nota(s) de R$ {nota}")
            valor %= nota

    if valor > 0:
        print(f"Resto não sacável (sem notas correspondentes): R$ {valor}")



saque = int(input("Digite o valor do saque: R$ "))

caixa_eletronico(saque)