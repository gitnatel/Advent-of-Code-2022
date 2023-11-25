f = open("02/input.txt")

opponent_moves = []
my_moves = []
moves = ['rock', 'paper', 'scissors']
move_score = {'rock': 1, 'paper': 2, 'scissors': 3}

base_scores = {'rock': 3, 'paper': 6, 'scissors': 0}
shifts = {'A': 0, 'B': 1, 'C': 2}
result_score = {}
for opponent_move, shift in shifts.items():
    for i, my_move in enumerate(base_scores.keys()):
        result_score[(opponent_move, my_move)] = base_scores[list(base_scores.keys())[(i + shift) % 3]]

f.seek(0)

for response in f:
    parts = response.strip().split(' ')
    opponent_moves.append(parts[0])
    my_moves.append(parts[1])

f.close()


total_games = len(opponent_moves)

def score_calc(opponent_move, my_move):  
    if opponent_move == "A": #rock
        if my_move == "rock":
            return move_score[my_move] + result_score[opponent_move, my_move]
        elif my_move == "paper":
            return move_score[my_move] + result_score[opponent_move, my_move]
        elif my_move == "scissors":
            return move_score[my_move] + result_score[opponent_move, my_move]
    if opponent_move == "B": #paper
        if my_move == "rock":
            return move_score[my_move] + result_score[opponent_move, my_move]
        elif my_move == "paper":
            return move_score[my_move] + result_score[opponent_move, my_move]
        elif my_move == "scissors":
            return move_score[my_move] + result_score[opponent_move, my_move]           
    if opponent_move == "C": #scissors
        if my_move == "rock":
            return move_score[my_move] + result_score[opponent_move, my_move]
        elif my_move == "paper":
            return move_score[my_move] + result_score[opponent_move, my_move]
        elif my_move == "scissors":
            return move_score[my_move] + result_score[opponent_move, my_move]

def score_over_all_games(opponent_moves, my_moves):
    total_score = 0
    for i in range(total_games):
        total_score += score_calc(opponent_moves[i], my_moves[i])
    return total_score

strategy_translation = []
for x in moves:
    for y in moves:
        for z in moves:
            if x != y and y != z and z != x:
                strategy_translation.append((x, y, z))

def best_score_possible():
    move_map = {'X': '', 'Y': '', 'Z': ''}
    max_score = 0

    for translation in strategy_translation:
        move_map['X'], move_map['Y'], move_map['Z'] = translation
        actual_my_moves = [move_map[move] for move in my_moves]
        total_score = score_over_all_games(opponent_moves, actual_my_moves)
        if total_score > max_score:
            max_score = total_score
    return max_score

print('The best score possible is: ' + str(best_score_possible()))