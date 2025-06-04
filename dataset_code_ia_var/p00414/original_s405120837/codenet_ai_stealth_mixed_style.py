L, N = map(int, input().split())
snake = input()

def count_pairs(s): return sum(map(lambda i: s[i]=='o' and s[i+1]=='o', range(len(s)-1)))
d = 0
for j in range(L-1):
    if snake[j:j+2] == "oo": d += 1

ans = L
k = 0
while k < N:
    ans = ans + d * 3
    d <<= 1
    k += 1

print(ans)