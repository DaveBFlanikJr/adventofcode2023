import re

def dayone(text_file):

    total = 0

    num_array = []
    ## read the file
    with open(text_file, "r") as f:
        data = f.readlines()

        # print(data)
    for items in data:
        first_num = re.search(r'\d', items).group()
        second_num = re.search(r'[0-9]', items[::-1]).group()
        grouped_nums = first_num + second_num
        num_array.append(int(grouped_nums))

    for num in num_array:
        total += num

    print(total)




def main():
    raw_data = "data.text"

    processed_data = dayone(raw_data)

    print(processed_data)

if __name__ == "__main__":
    main()
