### Advent of Code 2019 --- Day 1: The Tyranny of the Rocket Equation ---

with open(r"input.txt") as f:
    modules = [int(line.strip()) for line in f.readlines()]

def getFuel(n):
    return (n // 3) - 2

part1 = sum([getFuel(mass) for mass in modules])

part2 = list()
for i in modules:
    a = getFuel(i) 
    while a > 0:
        part2.append(a)
        a = getFuel(a)

part2 = sum(part2)

print('Puzzle 1: {a}\nPuzzle 2: {b}'.format(a=part1, b=part2))
