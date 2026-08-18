def verificaçao_de_voto():
    idade = int(input("Digite sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif idade == 16 or idade == 17:
        print("Voto opcional")
    elif 18 <= idade <= 69:
        print("Voto obrigatório")
    else:
        print("Voto opcional")


verificaçao_de_voto()