S = input()
count = 0
for w in S:
    if w == '+':
        count += 1
    else:
        count -= 1
print(count)