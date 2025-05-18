input()
a = list(map(int,input().split()))
input()
b = list(map(int,input().split()))

A = set(a)
B = set(b)

print(1 if B <= A else 0)