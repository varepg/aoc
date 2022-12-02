### problem 1 aoc 22

elf_counter = 0

calories = [0]

with open("input.txt", "r") as f:
    while line := f.readline():
        if line == "\n":
            elf_counter += 1
            calories.append(0)
        else:
            calories[elf_counter] += int(line)

max_value = max(calories)
total_top3 = 0

for i in range(3):
    idx, value = max(enumerate(calories), key=lambda v: v[1])
    total_top3 += value
    calories.pop(idx)

print(max_value)  # prints 72718
print(total_top3) # prints 213089