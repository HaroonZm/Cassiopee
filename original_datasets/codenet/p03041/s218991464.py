n, k = map(int, input().split())
s = str(input())
ans = s[:k-1]+ s[k-1].lower() + s[k:]

print(ans)