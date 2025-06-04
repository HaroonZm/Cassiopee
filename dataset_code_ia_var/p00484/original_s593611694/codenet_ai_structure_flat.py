from itertools import accumulate

n, k = map(int, input().split())
books = [[] for _ in range(10)]
while n:
    c, g = map(int, input().split())
    books[g - 1].append(c)
    n -= 1

books_acc = []
for q in books:
    s = sorted(q, reverse=True)
    acc = []
    for i, c in enumerate(s):
        acc.append(c + i * 2)
    acc2 = [0]
    total = 0
    for v in acc:
        total += v
        acc2.append(total)
    books_acc.append(acc2)

memo = [[-1 for _ in range(k + 1)] for _ in range(10)]
stack = []
stack.append((0, k))
result_table = {}
while stack:
    g, remain = stack[-1]
    key = (g, remain)
    if key in result_table:
        stack.pop()
        continue
    if g > 9:
        result_table[key] = 0
        stack.pop()
        continue
    if memo[g][remain] != -1:
        result_table[key] = memo[g][remain]
        stack.pop()
        continue
    book_acc = books_acc[g]
    salable = min(remain + 1, len(book_acc))
    subs = []
    skip = False
    for i in range(salable):
        next_key = (g + 1, remain - i)
        if next_key not in result_table:
            stack.append((g + 1, remain - i))
            skip = True
    if skip:
        continue
    for i in range(salable):
        v = book_acc[i] + result_table[(g + 1, remain - i)]
        subs.append(v)
    val = max(subs) if subs else 0
    memo[g][remain] = val
    result_table[key] = val
    stack.pop()
print(result_table[(0, k)])