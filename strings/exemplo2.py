#dividir uma srtring em partes
import urllib
from xml.sax.handler import feature_external_ges


def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input("Digite seu nome completo: ")
print(f'nome em partes: {separar_nome(nome_completo)[1]}')

#juntar strings
def criar_nome_completo(partes):
    nome_completo = ",".join(partes)
    return nome_completo

partes_nome = ["Luiza", "Polizel", "Casaqui"]
print(f'a juncao das partes do nome é {criar_nome_completo(partes_nome)}')

#verificar o inicio e o final de uma string
def analisar_url(url):
    inicia_com_https = url.startswith("https://")
    termina_com_br = url.startswith(".br")
    return inicia_com_https, termina_com_br

url = "https://www.gov.br"
tem_https, tem_br = analisar_url(url)
print(f'utiliza https? {analisar_url(url)}')
print(f'Termina com .br? {tem_br}')

#verificar se a string contem somente numeros
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print("o valor digitado e uma idade valida!")

    else:
        print("digite somente numeros inteiros")

idade = input("Digite sua idade: ")
validar_idade(idade)


#verificar se tem somente letras
def validar_nome(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
        print('o nome digitado e uma nome valido')


    else:
        print('digite um nome valido')

validar_nome(nome_completo)

#verificar se a string contem letras e numeros
def validar_usuario(usuario):
    usuario_valido = usuario.isalnum()
    if usuario_valido:
        print('usuario valido')
    else:
        print('utilize apenas letras e numeros')

nome_usuario = input("Digite seu usuario: ")
validar_usuario(nome_usuario)


#analisando uma frase
def analisar_frase(frase, palavra):
    frase_limpa = frase.strip()

    qtde_caracteres = len(frase_limpa)
    qtde_palavras = len(frase_limpa.split())
    ocorrencia_palavra = frase_limpa.count(palavra)

    print(f'frase completa: {frase_limpa}')
    print(f'total de caracteres: {qtde_caracteres}')
    print(f'total de palavras: {qtde_palavras}')
    print(f'ocorrencia de palavra pesquisada: {ocorrencia_palavra}')

frase_input = input("Digite uma frase: ")
ocorrencia_palavra = input("Digite uma palavra para contar a ocorrencia: ")
analisar_frase(frase_input, ocorrencia_palavra)






















