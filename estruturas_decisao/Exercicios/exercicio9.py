def calculadora_simples():


        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite qual conta quer fazer (+, -, * ou /): ")


        if operacao == '+':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacao == '-':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacao == '*':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacao == '/':
           resultado = num1 / num2
           print(f"Resultado: {num1} / {num2} = {resultado}")

        else:
            print("Operação inválida! Escolha entre +, -, * ou /.")

calculadora_simples()