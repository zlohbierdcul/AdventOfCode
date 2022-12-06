

def main():
    print(f"{get_marker(read_file(), 1)}")
    print(f"{get_marker(read_file(), 2)}")


def read_file():
    return open("./input.txt", "r").readline()


def check_for_dupes(sublist):
    if len(sublist) == len(set(sublist)):
        return False
    else:
        return True


def get_marker(datastream, part):
    if part == 1:
        z = 4
    else:
        z = 14
    for x in range(len(datastream) - z):
        sublist = []
        for y in range(z):
            sublist.append(datastream[x+y])
        # print(sublist)
        if not check_for_dupes(sublist):
            return x+y+1



main()

