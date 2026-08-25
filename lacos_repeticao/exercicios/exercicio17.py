def jogo_adivinhacao(numero_secreto):
    tentativas = 0
    acertou = False

    print("--- JOGO DA ADIVINHAÇÃO ---")
    print("Tente adivinhar o número secreto!")

    while not acertou:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            acertou = True
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR. Tente novamente.")
        else:
            print("O número secreto é MENOR. Tente novamente.")


segredo = 42
jogo_adivinhacao(segredo)