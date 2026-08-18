def aluno_aprovado():
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))

    media = (nota_1 + nota_2) / 2
    print(f'media: {media}')

    if media >= 7:
        print('aluno aprovado')
    elif media >= 5 and media < 7:
        print('aluno de recuperacao')
    else:
        print('aluno reprovado')

aluno_aprovado()


def login():

    email = 'luiza.polizel@gmail.com'
    senha = '2305'
    codigo_secreto = '1234'

    email_input = input('Digite seu email: ')
    senha_input = input('Digite sua senha: ')

    if email_input == email and  senha_input == senha:
        print('usuario logado')
        acessar_admin = input('Deseja acessar o administrador? (digite S ou N')
        if acessar_admin == 'S':
            codigo_secreto_input = input('Digite seu codigo secreto: ')
            if codigo_secreto_input == codigo_secreto:
                print('usuario logado')
            else:
                print('codigo incorreto')
        elif acessar_admin == 'N':
            print('usuario logado')
        else:
            print('usuario incorreto')

    else:
        print('usuario ou senha incorreto')

    login()

