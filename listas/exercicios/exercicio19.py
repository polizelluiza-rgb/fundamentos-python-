notas = [7.5, 6.0, 8.5, 9.0, 5.5]
def adicionar_nota(lista, nova_nota):
    lista.append(nova_nota)
    return lista
def inserir_nota(lista, nota, posicao):
    lista.insert(posicao, nota)
    return lista
def adicionar_varias_notas(lista, novas_notas):
    lista.extend(novas_notas)
    return lista
def remover_nota(lista, nota):
    if nota in lista:
        lista.remove(nota)
    else:
        print(f"A nota {nota} não foi encontrada na lista.")
    return lista
def remover_ultima_nota(lista):
    if len(lista) > 0:
        nota_removida = lista.pop()
        print(f"Nota removida: {nota_removida}")
    else:
        print("A lista está vazia!")
    return lista
def encontrar_posicao(lista, nota):
    if nota in lista:
        return lista.index(nota)
    else:
        print(f"A nota {nota} não está presente na lista.")
        return -1
def quantidade_notas(lista):
    return len(lista)
def ordenar_notas(lista):
    return sorted(lista)
def notas_invertidas(lista):
    return list(reversed(lista))
def somar_notas(lista):
    return sum(lista)
def calcular_media(lista):
    if len(lista) > 0:
        return sum(lista) / len(lista)
    return 0.0

print("Notas iniciais:", notas)

print("\n--- Testando as Funções ---")

adicionar_nota(notas, 10.0)
print("1. Após adicionar 10.0:", notas)

inserir_nota(notas, 8.0, 1)
print("2. Após inserir 8.0 na posição 1:", notas)

adicionar_varias_notas(notas, [4.5, 9.5])
print("3. Após adicionar [4.5, 9.5]:", notas)

remover_nota(notas, 6.0)
print("4. Após remover a nota 6.0:", notas)

remover_ultima_nota(notas)
print("5. Após remover a última nota:", notas)

pos = encontrar_posicao(notas, 8.5)
print(f"6. Posição da nota 8.5: índice {pos}")

qtd = quantidade_notas(notas)
print("7. Quantidade total de notas:", qtd)

notas_ord = ordenar_notas(notas)
print("8. Notas ordenadas (crescente):", notas_ord)

notas_inv = notas_invertidas(notas)
print("9. Notas em ordem inversa:", notas_inv)

soma = somar_notas(notas)
print(f"10. Soma total das notas: {soma:.2f}")

media = calcular_media(notas)
print(f"11. Média da turma: {media:.2f}")