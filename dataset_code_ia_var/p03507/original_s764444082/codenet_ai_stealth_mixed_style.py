from sys import stdin

def get_input():
    return stdin.readline()

N_K = get_input().split()
N = int(N_K[0])
K = int(N_K[1])
stuff = []
c = 0
while c < N:
    w, d = map(int, get_input().split())
    stuff.append((w, d))
    c += 1

def check(x): res = 0
for item in stuff:
    res += (max(0, ((x-item[0])//item[1])+1))
if res >= K:
    return 1
return 0

def run():
    right = 2*10**18
    left = 0
    s = right
    while abs(right-left) > 1:
        m = (right+left)//2
        if check(m): right = m
        else: left = m
    print(right)
    
run()