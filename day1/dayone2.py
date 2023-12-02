import re

def part_two(file_path):

    ## get the data
    with open(file_path, "r") as f:
        data = f.readlines()

    ## define the valid strings that count as numbers
    nums = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    first_last_digits = []

    for i, line in enumerate(data):
        line = line.rstrip("\n")
        digit = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        if len(digit) == 1:
            first_last_digits.append((digit[0], digit[0]))
        else:
            first_last_digits.append((digit[0], digit[-1]))

    arr = []
    for num in first_last_digits:
        num1 = num[0]
        num2 = num[1]

        tempstr = nums.get(num1, num1) + nums.get(num2, num2)
        arr.append(int(tempstr))

    print(sum(arr))


def main():
    file_path = "data.text"

    result = part_two(file_path)

    print(result)

if __name__ == "__main__":
    main()
