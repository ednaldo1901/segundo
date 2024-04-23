from itertools import combinations

# Função para obter os dados de um jogo
def obter_dados_jogo(numero_jogo):
    print(f"Digite os dados para o jogo {numero_jogo}:")
    equipe1_nome = input(f"Nome da equipe 1 do jogo {numero_jogo}: ")
    equipe1_odd = float(input(f"Odd da equipe 1 do jogo {numero_jogo}: "))
    equipe2_nome = input(f"Nom da equipe 2 do jogo {numero_jogo}: ")
    equipe2_odd = float(input(f"Odd da equipe 2 do jogo {numero_jogo}: "))
    return (equipe1_nome, equipe1_odd), (equipe2_nome, equipe2_odd)

# Obter os dados dos jogos
jogo1 = obter_dados_jogo(1)
jogo2 = obter_dados_jogo(2)

# Gerar todas as combinações possíveis entre os jogos
comb_jogos = [(jogo1[0], jogo2[0]), (jogo1[0], jogo2[1]), (jogo1[1], jogo2[0]), (jogo1[1], jogo2[1])]

# Exibindo as combinações de jogos e calculando o produto das odds
for i, (equipe1, equipe2) in enumerate(comb_jogos, start=1):
    produto_odds = equipe1[1] * equipe2[1]
    print("ig")
    print(f"Combinação {i}: {equipe1[0]} x {equipe2[0]}")
    print(f"Produto das odds: {produto_odds:.2f}\n")