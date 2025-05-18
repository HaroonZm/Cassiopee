n, m = [int(i) for i in input().split()]
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}

A = a & b
B = a | b

print('{} {}'.format(len(A),len(B)))
for a in sorted(A):
    print(a)
for b in sorted(B):
    print(b)