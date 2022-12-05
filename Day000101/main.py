def main():
    print(f"{get_answer(order_part_one(read_file()))}")
    print(f"{get_answer(order_part_two(read_file()))}")


def read_file():
    return open("input.txt", "r").read().split("\n\n")


def get_answer(new_stacks):
    answer = ""
    for stack in new_stacks:
        if stack:
            answer += stack.pop()
    return answer


def order_part_one(input_list):
    stacks, moves = input_list[0], input_list[1]
    formatted_stacks = get_stacks(stacks)
    return move_stacks_part_one(formatted_stacks, moves)


def order_part_two(input_list):
    stacks, moves = input_list[0], input_list[1]
    formatted_stacks = get_stacks(stacks)
    return move_stacks_part_two(formatted_stacks, moves)


def get_stacks(stacks_string):
    stacks = stacks_string.split("\n")
    formatted_stacks = []
    for stack in stacks:
        index = 0
        for x in range(1, len(stack), 4):
            formatted_stacks.append([])
            if stack[x].isupper():
                formatted_stacks[index].append(stack[x])
            index += 1
    for x in formatted_stacks:
        x.reverse()
    return formatted_stacks


def move_stacks_part_one(stacks, moves):
    moves_list = moves.split("\n")
    for move in moves_list:
        split_move = move.split()
        index = int(split_move[1])
        while index != 0:
            stacks[int(split_move[5]) - 1].append(stacks[int(split_move[3]) - 1].pop())
            index -= 1
    return stacks


def move_stacks_part_two(stacks, moves):
    moves_list = moves.split("\n")
    for move in moves_list:
        split_move = move.split()
        index = int(split_move[1])
        temp_storage = []
        while index != 0:
            temp_storage.append(stacks[int(split_move[3]) - 1].pop())
            index -= 1
        temp_storage.reverse()
        for x in temp_storage:
            stacks[int(split_move[5]) - 1].append(x)

    return stacks


main()
