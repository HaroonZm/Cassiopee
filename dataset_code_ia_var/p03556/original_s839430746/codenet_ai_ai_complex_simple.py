from functools import reduce

n = int(input())

def gen_sqrs(limit):
    i = 1
    while (sq := i*i) <= limit:
        yield sq
        i += 1

ans = reduce(lambda x, y: y, gen_sqrs(n), 0)

print(ans)