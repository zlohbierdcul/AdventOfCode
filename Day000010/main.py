

def main():
    print(f"{calculate_points(read_file())}")


def read_file():
    return open("./input.txt", "r").read()


# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# A for Rock, B for Paper, and C for Scissors (opponent)
# X for Rock, Y for Paper, and Z for Scissors (me)

def get_winning_points(my_move, your_move):
    if my_move == "X" and your_move == "C":
        return 6
    if my_move == "Z" and your_move == "B":
        return 6
    if my_move == "Y" and your_move == "A":
        return 6
    if my_move == "X" and your_move == "A":
        return 3
    if my_move == "Z" and your_move == "C":
        return 3
    if my_move == "Y" and your_move == "B":
        return 3
    else:
        return 0


# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

def get_move_points(move):
    if move == "X":
        return 1
    if move == "Y":
        return 2
    if move == "Z":
        return 3


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def get_strategy_move(my_strategy, your_move):
    if my_strategy == "X":
        if your_move == "A":
            return "Z"
        if your_move == "B":
            return "X"
        if your_move == "C":
            return "Y"

    if my_strategy == "Y":
        if your_move == "A":
            return "X"
        if your_move == "B":
            return "Y"
        if your_move == "C":
            return "Z"

    if my_strategy == "Z":
        if your_move == "A":
            return "Y"
        if your_move == "B":
            return "Z"
        if your_move == "C":
            return "X"


def calculate_points(strategy_list):
    move_list = strategy_list.split("\n")
    round_one_points = 0
    round_two_points = 0
    for move in move_list:
        split_move = move.split(" ")
        my_move = split_move[1]
        my_strategy = split_move[1]
        your_move = split_move[0]
        my_strategy_move = get_strategy_move(my_strategy, your_move)

        round_one_points += get_winning_points(my_move, your_move)
        round_one_points += get_move_points(my_move)

        round_two_points += get_winning_points(my_strategy_move, your_move)
        round_two_points += get_move_points(my_strategy_move)

    return [f"{round_one_points=}", f"{round_two_points=}"]


main()
