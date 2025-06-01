while True:
    n = input()
    if n == 0:
        break
    s = [map(int, raw_input().split()) for i in range(n)]  # read each row
    # smallest in each row
    min_in_rows = set(min(row) for row in s)
    # largest in each col (bit messy)
    max_in_cols = set(max(s[j][i] for j in range(n)) for i in range(n))
    result = list(min_in_rows & max_in_cols)
    if result:
        print(result[0])  # printing the 'lucky' number or whatever
    else:
        print(0)  # no luck this time