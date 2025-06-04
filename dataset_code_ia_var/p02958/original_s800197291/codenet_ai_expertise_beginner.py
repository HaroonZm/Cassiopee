n = int(input())
s = input().split()
for i in range(n):
    s[i] = int(s[i])

result = "YES"
problems = 0

for i in range(n - 1):
    if s[i + 1] - s[i] < 1:
        problems += 1
        if problems == 1:
            first_val = s[i]
            first_idx = i
        elif problems == 2:
            second_val = s[i + 1]
            second_idx = i + 1
        elif problems > 2:
            result = "NO"
            break

if problems == 1:
    result = "NO"
elif problems == 2:
    # swap the two elements
    temp = s[first_idx]
    s[first_idx] = s[second_idx]
    s[second_idx] = temp
    # check if the swap fixed the sequence
    ok = True
    if first_idx < n - 1:
        if s[first_idx + 1] - s[first_idx] < 1:
            ok = False
    if second_idx > 0:
        if s[second_idx] - s[second_idx - 1] < 1:
            ok = False
    if not ok:
        result = "NO"

print(result)