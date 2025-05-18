a, b = map(int, input().split())

d = a // b
r = a % b
f = a / b

print('{} {} {:.5f}'.format(d, r, f))