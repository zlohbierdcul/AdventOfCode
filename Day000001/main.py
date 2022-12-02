def main():
    find_elf(read_file())


def read_file():
    f = open("./list.txt", "r")
    return f.read()


def find_elf(calories_list):
    calories_per_elf = []
    elf_list = calories_list.split("\n\n")

    for elf in elf_list:
        cal = 0
        elf_cal = elf.split("\n")
        for calorie in elf_cal:
            cal += int(calorie)
        calories_per_elf.append(cal)

    index = calories_per_elf.index(max(calories_per_elf))
    sorted_list = sorted(calories_per_elf, reverse=True)

    print(f'{max(calories_per_elf)=}')
    top_three_calories = sorted_list[0] + sorted_list[1] + sorted_list[2]
    print(f'{top_three_calories=}')


main()
