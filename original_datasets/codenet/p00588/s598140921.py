from operator import add

pre = [
    ((0, 1, 2), (1, 0, 1), (2, 1, 0)),
    ((3, 2, 2), (2, 1, 1), (2, 1, 1)),
    ((1, 1, 2), (1, 1, 2), (2, 2, 3)),
    ((3, 2, 2), (2, 2, 2), (2, 2, 3)),
]

q = int(input())
for _ in range(q):
    n = int(input())
    books = [c == 'Y' for c in input()]
    books = [(0, 0)] + list(zip(books[:2 * n], books[2 * n:])) + [(0, 0)]
    shelves = [(u1 | u2) * 2 + (l1 | l2) for (u1, l1), (u2, l2) in zip(*[iter(books)] * 2)]
    ans = [0, 1, 2]
    for key in shelves:
        new_ans = [min(map(add, ans, costs)) for costs in pre[key]]
        ans = new_ans
    print(ans[0] + n)