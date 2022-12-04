### problem 3 part 2 aoc 22

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def priority_of_badge(r1, r2, r3):
    for char in r1:
        if char in r2 and char in r3:
            return 1 + chars.index(char)


total_priority = 0

with open("input.txt") as f:
    lines = f.readlines()

    group = []
    counter = 0
    for line in lines:
        if counter < 3:
            group.append(line)
            counter += 1
        else:
            total_priority += priority_of_badge(*group)
            group = [line]
            counter = 1
    # last group
    total_priority += priority_of_badge(*group)

print(total_priority) # prints 2525