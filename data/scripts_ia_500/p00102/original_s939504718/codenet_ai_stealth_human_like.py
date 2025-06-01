while True:
    n = int(input())
    if n == 0:
        break
    totals = [0] * (n + 1)  # cumulative sums including the row sum
    for _ in range(n):
        row = list(map(int, input().split()))
        row_sum = sum(row)
        row.append(row_sum)  # add sum at the end of the row
        for idx, val in enumerate(row):
            print(f"{val:5d}", end="")
            totals[idx] += val
        print()  # new line after each row
    # print the totals at the bottom
    for val in totals:
        print(f"{val:5d}", end="")
    print()  # blank line before next block (if any)