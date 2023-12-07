import re


def parse(file):
    with open(file, 'r') as f:
        data = f.readlines()

    values = []
    for line in data:
        numbers = re.findall(r'\d+', line)
        if numbers:
            whole_number = ''.join(numbers)
            values.append(int(whole_number))
    print(values)
    return values

def part_two(numbers):

    total = []

    for i in range(0, len(numbers), 2):
        time = numbers[i]
        distance = numbers[i + 1]
        count = 0

        for hold_time in range(1, time + 1):
            current_time = time - hold_time
            speed = hold_time
            #print(speed)
            current_distance = speed * current_time

            if current_distance > distance:
                count += 1
        total.append(count)
    print(total)
    return total

# data = parse('test.txt')
data = parse('data.txt')
game = part_two(data)
