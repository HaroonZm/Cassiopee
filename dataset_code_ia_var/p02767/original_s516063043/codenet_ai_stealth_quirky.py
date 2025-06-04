N = int(input())
X = [*map(int, input().split())]
solution = 1e99

i = 1
while i <= 100:
    err = sum((x - i)*(x - i) for x in X)
    if err < solution:
        solution = err
    i += 1

[*map(print, [solution])]