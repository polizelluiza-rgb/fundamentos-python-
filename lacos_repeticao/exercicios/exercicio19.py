def menu():
    opcao = 0

    while opcao != 4:
        print("\n--- MENU ---")
        print("1. Exibir números de 1 a 10")
        print("2. Exibir números pares de 1 a 10")
        print("3. Exibir tabuada")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            for i in range(1, 11):
                print(i)

        elif opcao == 2:
            for i in range(2, 11, 2):
                print(i)

        elif opcao == 3:
            num = int(input("Digite um número para ver a tabuada: "))
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")

        elif opcao == 4:
            print("Saindo do programa... Até mais!")

        else:
            print("Opção inválida! Tente novamente.")


# Chamada da função
menu()