import re

max_count = {
    'red': '12',
    'green': '13',
    'blue': '14'
}


def parsed_games(file):
    with open(file, 'r') as f:
        data = f.readlines()

    games = []
    for i, line in enumerate(data):
        line = line.strip('\n')
        sets = re.findall(r'(\d+)\s(blue|red|green)', line)
        game = []
        for pull in sets:
            game.append([pull[0], pull[1]])
        games.append(game)
    return games

def part_one(games):
    invalid_games = []

    for i, set in enumerate(games):
        for pull in set:
            color, count = pull[1], int(pull[0])

            if count > int(max_count[color]):
                invalid_games.append(i + 1)
                break
    return sum([i for i in range(1, len(games) + 1) if i not in invalid_games])

def part_two(games):
    total_result = 0
    for i, set in enumerate(games):
        max_counts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        result = 0
        for pull in set:
            color, count = pull[1], int(pull[0])

            if max_counts[color] < count:
                max_counts[color] = count
        result = max_counts["red"] * max_counts["green"] * max_counts["blue"]
        total_result += result
    print(total_result)

# games = parsed_games('test.text')
# games = parsed_games('data.text')
# print(part_one(games))

# test_games = parsed_games('test.text')
games = parsed_games('data.text')
part_two(games)
