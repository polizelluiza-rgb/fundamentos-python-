def calcular_idade(anos):
    meses = anos * 12
    dias = anos * 365

    print(f"Idade em anos: {anos}")
    print(f"Aproximadamente em meses: {meses} meses")
    print(f"Aproximadamente em dias: {dias} dias")

idade = int(input("Digite a idade em anos: "))
calcular_idade(idade)