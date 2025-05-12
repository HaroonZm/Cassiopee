n = int(input())
a = set(list(map(int, input().split())))
m = int(input())
b = set(list(map(int, input().split())))
for i in sorted(a-b):
    print(i)