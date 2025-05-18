n = int(input())

a = {int(i) for i in input().split()}

m = int(input())

b = {int(i) for i in input().split()}

c = tuple(sorted(a-b))

for i in c:
    print(i)