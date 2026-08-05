
preco_arroz = 26.90
preco_feijao = 8.50
preco_cafe = 39.90

total = preco_arroz + preco_feijao + preco_cafe
media = total / 3

produto_mais_caro = "Café"
valor_mais_caro = preco_cafe

print(f"Total da compra: R$ {total:.2f}")
print(f"Média dos preços: R$ {media:.2f}")
print(f"Produto mais caro: {produto_mais_caro} (R$ {valor_mais_caro:.2f})")