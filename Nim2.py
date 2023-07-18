import json
import yaml
import random

maxpos = 1000
nr_games = [10, 100, 1000, 10000]

# Stat:
# two-dimensional dictionary holding the statistical analysis of each move
# Stat[position][move], initialized with 0
# For each simulated game:
# - gains one point if move at position ended in winning the game
# - loses one point if move at position ended in losing the game

Stat = {}
for i in range(1, maxpos + 1):
    Stat[i] = {}
    for j in range(1, min(i, 3) + 1):
        Stat[i][j] = 0

for game_count in nr_games:
    for g in range(game_count):
        moves = {}
        moves[1] = {}
        moves[2] = {}
        pos = maxpos
        player = 0
        while pos:
            player = 2 if player == 1 else 1
            best_moves = [move for move in Stat[pos] if Stat[pos][move] == max(Stat[pos].values())]
            move = random.choice(best_moves)
            moves[player][pos] = move
            pos -= move
        for pos in moves[player]:
            Stat[pos][moves[player][pos]] += 1
        player = 2 if player == 1 else 1
        for pos in moves[player]:
            Stat[pos][moves[player][pos]] -= 1

    # Perform final evaluation
    def evaluate_moves(Stat):
        best_moves = {}
        for i in range(1, maxpos + 1):
            best_move = max(Stat[i], key=Stat[i].get)
            best_moves[i] = best_move
        return best_moves

    # Automated evaluation of learning limit
    def detect_learning_limit(Stat):
        for i in range(maxpos, 0, -1):
            correct_move = i % 4
            if correct_move == 0:
                correct_move = 3
            best_move = best_moves[i]
            if best_move != correct_move:
                return i
        return 0

    best_moves = evaluate_moves(Stat)
    learning_limit = detect_learning_limit(Stat)

    print(f"Game Count: {game_count}\tLearning Limit: {learning_limit}")

    # Save Stat in json and yaml file:
    with open(f'nim_{game_count}_games.json', 'w') as f:
        json.dump(Stat, f, sort_keys=True, indent=4, separators=(',', ': '))

    with open(f'nim_{game_count}_games.yaml', 'w') as f:
        f.write(yaml.dump(Stat))


"""
No código modificado, ao selecionar o melhor movimento para uma posição, é verificado se há vários 
movimentos com a mesma pontuação mais alta usando uma list comprehension. Em seguida, um movimento é 
escolhido aleatoriamente da lista de melhores movimentos usando random.choice().

Esse mecanismo garante que, quando houver vários melhores movimentos, o programa selecionará um movimento 
aleatório entre eles, eliminando qualquer viés em direção à primeira opção.

Em relação à eficiência do processo de aprendizado, introduzir aleatoriedade na escolha entre movimentos 
igualmente bons pode ser benéfico. Isso ajuda a explorar diferentes caminhos durante a fase de aprendizado e 
impede que o algoritmo fique preso em uma única estratégia determinística. Essa aleatoriedade adiciona um 
elemento de exploração, potencialmente melhorando o processo de aprendizado ao descobrir melhores movimentos 
e estratégias.
"""