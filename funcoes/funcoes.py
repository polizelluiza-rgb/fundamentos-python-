def exibir_mensagem():
    print('hello world')

def somar():
    valor1 = 50
    valor2 = 60
    total = valor1 + valor2
    print(f'A soma vale {total}')

def calcular_media():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    return media

exibir_mensagem()
somar()

nota_final = calcular_media()
print(f'a nota final do aluno foi {nota_final}') 