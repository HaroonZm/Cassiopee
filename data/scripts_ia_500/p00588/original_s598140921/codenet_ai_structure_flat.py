from operator import add
q = int(input())
for _ in range(q):
    n = int(input())
    books = [c == 'Y' for c in input()]
    books = [(0, 0)] + list(zip(books[:2 * n], books[2 * n:])) + [(0, 0)]
    shelves = []
    i = 0
    while i < len(books) - 1:
        u1 = books[i][0]
        l1 = books[i][1]
        u2 = books[i + 1][0]
        l2 = books[i + 1][1]
        key = (u1 | u2) * 2 + (l1 | l2)
        shelves.append(key)
        i += 2
    ans = [0, 1, 2]
    for key in shelves:
        new_ans = []
        for costs in [
            (0, 1, 2),
            (1, 0, 1),
            (2, 1, 0),
            (3, 2, 2),
            (2, 1, 1),
            (2, 1, 1),
            (1, 1, 2),
            (1, 1, 2),
            (2, 2, 3),
            (3, 2, 2),
            (2, 2, 2),
            (2, 2, 3),
        ][key]:
            sum_vals = []
            j = 0
            while j < 3:
                sum_vals.append(ans[j] + costs[j])
                j += 1
            new_ans.append(min(sum_vals))
        ans = new_ans
    print(ans[0] + n)