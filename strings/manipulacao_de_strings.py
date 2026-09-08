
# Converter texto para maiúsculas e minúsculas
def formatar_nome(nome):
    # nome em maiúsculo:
    nome_maiusculo = nome.upper()

    # nome minúsculo:
    nome_minusculo = nome.lower()

    # nome com primeira letra maiúscula:
    nome_camel_case = nome.capitalize()

    return (nome_maiusculo, nome_minusculo, nome_camel_case)

nome = input("Digite seu nome: ")

# print(formatar_nome(nome)[1])

banana, batata, cebola = formatar_nome(nome)
print(f"Nome maiúsculo: {banana}")
print(f"Nome minúsculo: {batata}")
print(f"Nome Camel Case: {cebola}")

# remover espaços desnecessários
def limpar_texto(texto):
    #remove espaços no inicio e final do texto
    texto_limpo = texto.strip()
    # Remove espaços da esquerda .lstrip()
    # Remove espaçoes da direita .rstrip()
    return texto_limpo

texto_1 = "    Aprender Python é legal!!!!     "
print(f"Texto antes: {texto_1}")
print(f"Texto depois: {limpar_texto(texto_1)}")

# Substituir Palavras
def trocar_cidade(cidade):
    # Troca uma palavra por outra
    texto_trocado = cidade.replace(cidade, "Piracicaba")
    return texto_trocado

cidade = input("Digite a cidade que voce mora: ")
print(f"Eu moro em: {trocar_cidade(cidade)}")

# Contar caracteres ou ocorrencias
def analisar_texto(texto, letra):
    # contar a quantidade de caracteres
    qtde_caracteres = len(texto)

    # contar a quantidade de ocorrencias
    qtde_letra = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letra

texto_2 = input("Digite um texto: ")
letra = input("Digite uma letra: ")
caracteres, letras = analisar_texto(texto_2, letra)

print(f"Total de caracteres: {caracteres}")
print(f"Total de letras pesquisadas: {letras}")

# Verificar se uma palavra está presente
def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    # Retorna um booleano (True ou False)
    return palavra_presente

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print(f"A palavra está presente na frase? {verificar_palavra(frase, palavra)}")

# Encontrar a posição de uma palavra
def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

frase_2 = input("Digite uma nova frase: ")
palavra_2 = input("Digite uma palavra para saber sua posicao: ")

print(f"A posição da palavra é {encontrar_posicao_palavra(frase_2, palavra_2)}")



















