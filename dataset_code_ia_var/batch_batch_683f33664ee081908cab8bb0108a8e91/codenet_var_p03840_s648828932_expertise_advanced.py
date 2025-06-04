from sys import stdin

I, O, _, J, L, *_ = map(int, stdin.readline().split())

def even_floor_sum(*args):
    return sum(x - (x & 1) for x in args)

ans1 = O + even_floor_sum(I, J, L)
ans2 = 0
if all([I, J, L]):
    ans2 = 3 + O + even_floor_sum(I - 1, J - 1, L - 1)
print(max(ans1, ans2))