input()
a, d = map(int, input().split())
x = [tuple(map(int, input().split())) for _ in range(int(input()))]
k = int(input())
for i in x[::-1]:
    if i[0] == 1:
        if i[1] == k:
            k = i[2]
    else:
        if i[1] == k:
            k = i[2]
        elif i[2] == k:
            k = i[1]
print(a + d * (k - 1))