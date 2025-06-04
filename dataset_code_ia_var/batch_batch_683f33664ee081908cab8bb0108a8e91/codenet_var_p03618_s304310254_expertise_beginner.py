s = input()
n = len(s)
cnt = 0
for char in set(s):
    count = s.count(char)
    if count >= 2:
        cnt += count * (count - 1) // 2
print(n * (n - 1) // 2 - cnt + 1)