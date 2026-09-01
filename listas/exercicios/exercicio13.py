def adicionar_cliente(fila, cliente):

    fila.append(cliente)

def atender_cliente(fila):

    if len(fila) > 0:

        cliente_atendido = fila.pop(0)
        return cliente_atendido
    else:
        print("A fila está vazia! Nenhum cliente para atender.")
        return None

fila_clientes = []
while True:
    nome_cliente = input("Digite o nome do cliente (ou 'sair' para encerrar a inserção): ")

    if nome_cliente.lower() == 'sair':
        break

    adicionar_cliente(fila_clientes, nome_cliente)
    print(f"Fila atual: {fila_clientes}")

print("\n--- Atendimento dos Clientes ---")

while len(fila_clientes) > 0:
    atendido = atender_cliente(fila_clientes)
    print(f"Cliente atendido: {atendido}")
    print(f"Fila restante: {fila_clientes}")

print("Todos os clientes foram atendidos com sucesso!")