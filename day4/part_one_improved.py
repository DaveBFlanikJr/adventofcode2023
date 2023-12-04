import re

def parse(file):
  cards = []
  with open(file) as f:
    lines = f.readlines()
    for line in lines:
      str = re.sub(r'Card\s+\d+:', '', line.strip("\n")).split(" | ")
      for card in str:
        nums = re.findall("\d+", card)
        cards.append([int(i) for i in nums])
        ## we are creating a serires of 2d arrays (par of 2d arrays)
    return [cards[i:i+2] for i in range(0, len(cards), 2)]

## Other soludtion (not mine but much easier to read)
def part_one(cards):
    points = []
    score = 0

    ## gets us the nested list
    for i in range(0, len(cards)):
        # print(cards[i])
        ## will grab the numbers in the the second nested array (our numbers)
        for num in cards[i][1]:
            ## will check if the score for the card is zero and if our number matches the winning number (at array[0])
            if score == 0 and num in cards[i][0]:
                score += 1
            elif score != 0 and num in cards[i][0]:
                score *= 2
        points.append(score)
        score = 0
    return sum(points)
cards = parse('test.text')
game_1 = part_one(cards)
