n, k = input().split()
n = int(n)
k = int(k)

books = []
for i in range(10):
    books.append([])

for _ in range(n):
    c, g = input().split()
    c = int(c)
    g = int(g)
    books[g - 1].append(c)

for i in range(10):
    books[i].sort(reverse=True)

books_acc = []
for q in books:
    acc = [0]
    total = 0
    for i in range(len(q)):
        total += q[i] + i * 2
        acc.append(total)
    books_acc.append(acc)

memo = []
for i in range(10):
    memo.append([-1] * (k + 1))

def combi(g, remain):
    if g == 10:
        return 0
    if memo[g][remain] != -1:
        return memo[g][remain]

    best = 0
    max_take = min(remain, len(books_acc[g]) -1)
    for i in range(max_take + 1):
        val = books_acc[g][i] + combi(g + 1, remain - i)
        if val > best:
            best = val

    memo[g][remain] = best
    return best

print(combi(0, k))