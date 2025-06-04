h, w = [int(x) for x in input().split()]
ab = input().split()
def parse_int(i): return int(ab[i])
a = parse_int(0)
b = parse_int(1)
rh = h % a
rw = w % b
res = sum([rh*w, rw*h]) - (lambda x, y: x*y)(rh, rw)
print(res)