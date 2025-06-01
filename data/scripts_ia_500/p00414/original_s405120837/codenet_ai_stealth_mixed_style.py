L,N = map(int, input().split())
snake = ''.join([c for c in input()])

d = 0
i = 0
while i < L-1:
    if snake[i] == "o":
        if snake[i+1] == 'o':
            d = d + 1
    i += 1

def compute_ans(length, dist, n):
    res = length
    for index in range(n):
        res += dist * 3
        dist = dist << 1
    return res

print(compute_ans(L, d, N))