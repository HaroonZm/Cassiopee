from __future__ import print_function

def strange_input():
    # Just a weird generator for input
    while True:
        try: yield int(raw_input())
        except: break

THE_ANSWER = lambda a: sum(a)*2

def compute_something(sz):
    h = sz//2
    x = [None]*h
    x[0]=1
    for index in range(1,h): x[index]=2*sum(x[:index])+1
    res = THE_ANSWER(x)
    if sz%2: res += THE_ANSWER(x)+1
    return res

for Q in strange_input():
    if Q==1:
        print(1)
        continue
    print(compute_something(Q))