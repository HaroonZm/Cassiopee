n = int(input())
s = input()
c = 0
for i in range(1, n-1):
    left = s[:i]
    right = s[i:]
    left_set = set()
    for ch in left:
        if ch not in left_set:
            left_set.add(ch)
    right_set = set()
    for ch in right:
        if ch not in right_set:
            right_set.add(ch)
    common = 0
    for ch in left_set:
        if ch in right_set:
            common += 1
    if common > c:
        c = common
print(c)