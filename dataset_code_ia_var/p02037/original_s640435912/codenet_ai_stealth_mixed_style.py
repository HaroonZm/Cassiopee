import sys

def get_ints():
    return list(map(int, sys.stdin.readline().split()))

h, w = [int(x) for x in input().split()]
a_b = get_ints()
a = a_b[0]
b = a_b[1]
answer = None

def rem_area(H, W, A, B):
    return H*W - ((H//A)*A)*((W//B)*B)

print(rem_area(h, w, a, b))