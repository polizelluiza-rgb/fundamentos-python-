def inserir_aluno(alunos, nome, posicao):

    alunos.insert(posicao, nome)


    print("Lista de alunos atualizada:", alunos)


lista_alunos = ["Camila", "Manu", "Maria"]

novo_aluno = input("Digite o nome do aluno: ")
posicao_inserir = int(input("Digite a posição em que deseja inseri-lo (índice numérico): "))


inserir_aluno(lista_alunos, novo_aluno, posicao_inserir)