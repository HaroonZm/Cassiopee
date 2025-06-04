_ = input()
A = input().split()
count = 0
for x in A:
    if int(x) % 2 == 0:
        count += 1
print(count)