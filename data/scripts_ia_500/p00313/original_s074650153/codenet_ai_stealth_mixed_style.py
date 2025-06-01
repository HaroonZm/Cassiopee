n = int(input())
a = input().split()
a.pop(0)
b = list(map(int, input().split()))
b = b[1:]
c = [int(x) for x in input().split()][1:]
count = 0
i = 0
while i < n:
    i += 1
    if c.__contains__(i) and (i not in a or i in b):
        count = count + 1
print(count)