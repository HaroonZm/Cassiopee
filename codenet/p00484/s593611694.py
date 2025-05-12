from itertools import accumulate

n, k = map(int, input().split())
books = [[] for _ in range(10)]

while n:
    c, g = map(int, input().split())
    books[g - 1].append(c)
    n -= 1

books_acc = [[0] + list(accumulate(c + i * 2 for i, c in enumerate(sorted(q, reverse=True)))) for q in books]

def memoize(f):
    memo = [[-1] * (k + 1) for _ in range(10)]

    def main(x, y):
        if x > 9:
            return 0
        result = memo[x][y]
        if result < 0:
            result = memo[x][y] = f(x, y)
        return result

    return main

@memoize
def combi(g, remain):
    book_acc = list(books_acc[g])
    salable = min(remain + 1, len(book_acc))
    return max([book_acc[i] + combi(g + 1, remain - i) for i in range(salable)], default=0)

print(combi(0, k))