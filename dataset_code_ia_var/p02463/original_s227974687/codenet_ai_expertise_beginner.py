n = int(input())
a = input().split()
a_set = set()
for num in a:
    a_set.add(int(num))

m = int(input())
b = input().split()
b_set = set()
for num in b:
    b_set.add(int(num))

union_set = a_set | b_set
result = list(union_set)
result.sort()

for i in result:
    print(i)