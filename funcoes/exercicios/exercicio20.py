def cadastrar_usuario():

    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    profissao = input("Digite a sua profissão: ")
    cidade = input("Digite a sua cidade: ")

    print("\n" + "=" * 30)
    print("      FICHA DE CADASTRO      ")
    print("=" * 30)
    print(f"Nome:      {nome}")
    print(f"Idade:     {idade} anos")
    print(f"Profissão: {profissao}")
    print(f"Cidade:    {cidade}")
    print("=" * 30)


cadastrar_usuario()