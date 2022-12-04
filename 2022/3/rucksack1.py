### problem 3 part 1 aoc 22

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def priority_of_duplet(c1, c2):
    for char in c1:
        if char in c2:
            return 1 + chars.index(char)


total_priority = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        c1 = line[: len(line)//2]
        c2 = line[len(line)//2: ]

        total_priority += priority_of_duplet(c1, c2)

print(total_priority) # prints 7581