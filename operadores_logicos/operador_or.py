# Operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input(f"voce tem dinheiro para comprar? "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"vou comer um japones hoje?: {autorizado}")

posso_comprar()