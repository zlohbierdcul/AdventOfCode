

def main():
    print(f"{calculate_intersecting_pairs(read_file())}")


def read_file():
    return open("input.txt", "r").read().split("\n")


def calculate_intersecting_pairs(pair_list):
    pairs = get_pairs(pair_list)
    intersecting_pairs = 0
    overlapping_pairs = 0
    for pair in pairs:
        if is_overlapping(pair):
            overlapping_pairs += 1
        if is_intersections(pair):
            intersecting_pairs += 1
            print(f"{intersecting_pairs=}")
    return [intersecting_pairs, overlapping_pairs]


# Method converts ill formatted list of pairs in list of sets, with each set representing all sections of that elf
def get_pairs(pair_list):
    pairs = []
    for pair in pair_list:
        split_pairs = pair.split(",")
        # ['2-4','6-8']
        pair1 = split_pairs[0].split("-")
        pair2 = split_pairs[1].split("-")
        # creating a set that contains all int numbers representing the sections of the elves
        set_pair1 = set(range(int(pair1[0]), int(pair1[1]) + 1))
        set_pair2 = set(range(int(pair2[0]), int(pair2[1]) + 1))
        reformatted_pair = [set_pair1, set_pair2]
        pairs.append(reformatted_pair)
    return pairs


# check if the sets of the two elves overlap
def is_overlapping(pair):
    return bool(set(pair[0]) & set(pair[1]))


# check if the two sets are a subset of each other, if so, one is fully contained in the other one
def is_intersections(pair):
    return pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])


main()

