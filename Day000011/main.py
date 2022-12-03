import re


def main():
    print(f"{calculate_priority(read_file())}")
    print(f"{calculate_badge_priority(read_file())}")


def read_file():
    return open("./input.txt", "r").read()


def calculate_priority(backpack_input):
    backpack_list = backpack_input.split("\n")
    total_prio = 0
    for backpack in backpack_list:
        first_compartment, second_compartment = backpack[:(len(backpack) // 2)], backpack[(len(backpack) // 2):]
        common_item = set(first_compartment).intersection(second_compartment).pop()
        total_prio += get_prio(common_item)
    return total_prio


def calculate_badge_priority(backpack_input):
    group_list = get_group_list(backpack_input.split("\n"))
    total_prio = 0
    for group in group_list:
        common_item = set(group[0]).intersection(group[1], group[2]).pop()
        total_prio += get_prio(common_item)
    return total_prio


def get_group_list(backpack_list):
    group_list = []
    for x in range(0, len(backpack_list), 3):
        group = [backpack_list[x], backpack_list[x + 1], backpack_list[x + 2]]
        group_list.append(group)
    return group_list


def get_prio(item):
    reg_large = re.compile(r"[A-Z]")
    reg_small = re.compile(r"[a-z]")
    if re.match(reg_small, item):
        return ord(item) - 96
    elif re.match(reg_large, item):
        return ord(item) - 38


main()
