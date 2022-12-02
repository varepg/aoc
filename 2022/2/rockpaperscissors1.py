### problem 2 part 1 aoc 22

moves = ["X", "Y", "Z"]

alias = {
    "A": "X", # rock
    "B": "Y", # paper
    "C": "Z" # scissors
}


def p2_points(p1, p2):
    idx = moves.index(p2)
    score = idx+1
    if p1 == moves[idx-1]:
        return score + 6 
    elif p2 == p1:
        return score + 3
    else:
        return score


p2_total = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        p1 = alias[line[0]]
        p2 = line[2]
        p2_total += p2_points(p1, p2)

print(p2_total) # 11475
