import json
import yaml
import random

rows = [1, 3, 5, 7]
nr_games = [10, 100, 1000, 10000]

# Stat:
# two-dimensional dictionary holding the statistical analysis of each move
# Stat[row][move], initialized with 0
# For each simulated game:
# - gains one point if move on a row ended in winning the game
# - loses one point if move on a row ended in losing the game

Stat = {}
for i in range(len(rows)):
    Stat[i] = {}
    for j in range(1, rows[i] + 1):
        Stat[i][j] = 0

for game_count in nr_games:
    for g in range(game_count):
        moves = {}
        for i in range(len(rows)):
            moves[i] = {}
        player = 0
        while any(rows):
            player = 1 - player
            non_empty_rows = [i for i in range(len(rows)) if rows[i] > 0]
            if not non_empty_rows:
                break
            row = random.choice(non_empty_rows)
            best_moves = [move for move in Stat[row] if Stat[row][move] == max(Stat[row].values())]
            move = random.choice(best_moves)
            moves[row][rows[row]] = move
            rows[row] -= move
        for i in range(len(rows)):
            for row in moves[i]:
                Stat[i][moves[i][row]] += 1 if player == i else -1

    # Perform final evaluation
    def evaluate_moves(Stat):
        best_moves = {}
        for i in range(len(rows)):
            best_move = max(Stat[i], key=Stat[i].get)
            best_moves[i] = best_move
        return best_moves

    # Automated evaluation of winning strategy
    def detect_winning_strategy(rows):
        xor_sum = 0
        for row in rows:
            xor_sum ^= row
        return xor_sum != 0

    best_moves = evaluate_moves(Stat)
    has_winning_strategy = detect_winning_strategy(rows)

    print(f"Game Count: {game_count}")
    if has_winning_strategy:
        print("The game has a winning strategy!")
        print("Winning Moves:")
        for i in range(len(rows)):
            print(f"Row {i+1}: Take {best_moves[i]} pieces")
    else:
        print("The game does not have a winning strategy.")
    print()

# Save Stat in json and yaml files:
with open('nim_game_analysis.json', 'w') as f:
    json.dump(Stat, f, sort_keys=True, indent=4, separators=(',', ': '))

with open('nim_game_analysis.yaml', 'w') as f:
    f.write(yaml.dump(Stat))
