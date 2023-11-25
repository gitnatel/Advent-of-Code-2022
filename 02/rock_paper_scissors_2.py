f = open("02/input.txt")

opponent_moves = []
my_moves = []

f.seek(0)

for response in f:
    parts = response.strip().split(' ')
    opponent_moves.append(parts[0])
    my_moves.append(parts[1])

f.close()

def score_calc(opponent_move, my_move):  
    if opponent_move == "A": #rock
        if my_move == "X": #lose
            return 3
        elif my_move == "Y": #draw
            return 4
        elif my_move == "Z": #win
            return 8
    if opponent_move == "B": #paper
        if my_move == "X":
            return 1
        elif my_move == "Y":
            return 5
        elif my_move == "Z":
            return  9      
    if opponent_move == "C": #scissors
        if my_move == "X":
            return 2
        elif my_move == "Y":
            return 6
        elif my_move == "Z":
            return 7

total_games = len(opponent_moves)


def score_over_all_games(opponent_moves, my_moves):
    total_score = 0
    for i in range(total_games):
        total_score += score_calc(opponent_moves[i], my_moves[i])
    return total_score

print("your score is: " + str(score_over_all_games(opponent_moves, my_moves)))