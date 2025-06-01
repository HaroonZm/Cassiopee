n = int(input())
a = input().split()
X = int(a[0])
a = set(map(int, a[1:]))

b_raw = input().split()
Y = int(b_raw[0])
b = set()
for val in b_raw[1:]:
    b.add(int(val))

c_list = list(map(int, input().split()))
Z, *c_rest = c_list
c = set(c_rest)

a_bar = set()
for number in range(1, n+1):
    if number not in a:
        a_bar.add(number)

ans = (a_bar.intersection(c)).union(b.intersection(c))
print(len(ans))