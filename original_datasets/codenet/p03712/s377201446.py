a, b = map(int, input().split())

s = []
for i in range(a):
    s.append(input())

print("#" * (b + 2))
for i in range(a):
    print("#" + s[i] + "#")

print("#" * (b + 2))