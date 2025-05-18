n = int(input())
li = []

for i in range(n):
    l = list(map(int, input().split()))
    li.append(l)

li = sorted(li)

for i in li:
    print(" ".join(map(str, i)))