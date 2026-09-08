def separar_dados(string_dados):
    dados_lista = string_dados.split(",")
    print(f"Nome: {dados_lista[0]}")
    print(f"Idade: {dados_lista[1]}")
    print(f"Profissão: {dados_lista[2]}")
    print(f"Cidade: {dados_lista[3]}")

dados = "João,40,Desenvolvedor,Piracicaba"

separar_dados(dados)