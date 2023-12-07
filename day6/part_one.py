import re
from functools import reduce


def parse(file):
    with open (file, 'r') as f:
        data = f.readlines()

    lines = []
    for line in data:
        digits = [int(x) for x in line.split()[1:]]
        lines.append(digits)

    transposed_lines = []
    for i in range(len(lines[0])):
        temp = []
        for line in lines:
            temp.append(line[i])
        transposed_lines.append(temp)
    return transposed_lines

def part_one(lines):
    total = []

    for line in lines:
        time, distance = line[0], line[1]
        count = 0

        for hold_time in range(1, time + 1):
            current_time = time - hold_time

            speed = hold_time
            current_distance = speed * current_time

            if current_distance > distance:
                count += 1
        total.append(count)

    final_score = reduce(lambda x, y: x*y, total)
    print(final_score)
    return final_score

# data = parse('test.txt')
data = parse('data.txt')
game = part_one(data)
