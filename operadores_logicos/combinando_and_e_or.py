# Operadores anf e not

def posso_entrar_no_show_do_enhypen():
    POSSUI_INGRESSO = True
    idade = int(input('qual a sua idade? '))
    nome_esta_na_lista = bool(input('qual a sua nome_esta_na_lista? '))

    posso_entrar = (nome_esta_na_lista or POSSUI_INGRESSO) and idade >= 18

    print(f'vou conseguir entrar no show? {posso_entrar}')

posso_entrar_no_show_do_enhypen()