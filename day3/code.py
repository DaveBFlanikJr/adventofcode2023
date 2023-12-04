## So what we know ##

## All Numbers that are adjacent (next to, above, below, diagonal) a symbol count
## . do not count as a symbol, but the others do (*, #, +, $)
## We can get the total by getting the sum of the valid numbers


with open("data.text") as fin:
    data = fin.read()
    lines = data.strip().split('\n')

n_rows = len(lines)
n_columns = len(lines[0])

def is_symbol(i, j):
    if not (0 <= i < n_rows and 0 <= j < n_columns):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()

ans = 0

for i, line in enumerate(lines):
    start = 0

    j = 0

    while j < n_columns:
        start = j
        num = ""
        while j < n_columns and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        if is_symbol(i, start-1) or is_symbol(i,j):
            ans += num
            continue
        for k in range(start-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                ans += num
                break
print(ans)
