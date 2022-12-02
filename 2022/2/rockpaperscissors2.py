### problem 2 part 2 aoc 22

moves = ["A", "B", "C"]


def p2_points(p1, p2):

    idx = moves.index(p1)

    match p2:
        case "X": return (idx-1)%3 + 1 + 0
        case "Y": return idx + 1 + 3
        case "Z": return (idx + 1)%3 + 1 + 6


p2_total = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        p1 = line[0]
        p2 = line[2]
        p2_total += p2_points(p1, p2)

print(p2_total) # prints 16862