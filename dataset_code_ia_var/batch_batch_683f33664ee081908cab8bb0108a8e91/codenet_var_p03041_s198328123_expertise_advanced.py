n, k = map(int, input().split())
s = input()
print(f"{s[:k-1]}{s[k-1].lower()}{s[k:]}")