L, R, d = map(int, input().split())
count = 0
while L != R+1:
    if L%d == 0:
        count += 1
    L += 1
print(count)