n = int(input())
s = list(input())

max_count = 0
for i in range(n + 2):
    left = s[0:i]
    right = s[i:n+1]
    common = []
    for letter in left:
        if letter in right and letter not in common:
            common.append(letter)
    if len(common) >= max_count:
        max_count = len(common)
print(max_count)