n, k = map(int, input().split())
s = list(input())
s[k-1] = s[k-1].lower()
i = 0
while i < n:
    print(s[i], end="")
    i += 1