def analisar_temperaturas(temperaturas):

    quantidade = len(temperaturas)
    soma = sum(temperaturas)

    media = soma / quantidade if quantidade > 0 else 0
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas

lista_temperaturas = []
qtd_leituras = int(input("Quantas temperaturas deseja informar? "))

for i in range(qtd_leituras):
    temp = float(input(f"Digite a temperatura {i + 1} (°C): "))
    lista_temperaturas.append(temp)

qtd, soma_total, media_temp, temps_ordenadas = analisar_temperaturas(lista_temperaturas)

print("\n--- Relatório de Temperaturas ---")
print(f"Quantidade de leituras: {qtd}")
print(f"Soma das temperaturas: {soma_total:.1f}°C")
print(f"Média das temperaturas: {media_temp:.2f}°C")
print(f"Temperaturas ordenadas: {temps_ordenadas}")