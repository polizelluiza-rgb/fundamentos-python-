def criar_ranking(pontuacoes):

    ranking = sorted(pontuacoes, reverse=True)
    return ranking

lista_pontuacoes = [150, 450, 80, 1200, 320, 950]

print("Pontuações registradas:", lista_pontuacoes)

ranking_final = criar_ranking(lista_pontuacoes)

print("Ranking de pontuações (da maior para a menor):", ranking_final)