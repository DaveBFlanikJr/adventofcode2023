

## We will have cards with numbers seperated by a |
# left hand side is the winning numbers right hand side is mine
# We need to itterate over the numbers on the left, grab a diget and check if its a number we have
# if yes then we add 1 to our score, if no then we move on


with open('data.text') as fin:
    data = fin.read()
    cards = data.strip().split('\n')

card_lists = [card.split(':') for card in cards]

card_content_lists = [[card[0]] + card[1].split('|') for card in card_lists]

games = [[content[0]] + [list(map(int, numbers.split())) for numbers in content[1:]] for content in card_content_lists]

matches_count = {}

total = 0

for game in games:
    winning_numbers = game[1]
    my_numbers = game[2]

    # Calculate the score based on the number of winning numbers
    score = 2 ** (len(set(winning_numbers) & set(my_numbers)) - 1) if set(winning_numbers) & set(my_numbers) else 0

    # Print the result for the current game
    # print(f"Winning Numbers: {winning_numbers}")
    # print(f"My Numbers: {my_numbers}")
    # print(f"Score: {score}")
    # print()
    total += score

print(total)
