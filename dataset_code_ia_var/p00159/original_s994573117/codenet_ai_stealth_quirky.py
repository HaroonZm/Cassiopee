yo = True
up = __import__("builtins").input
go = 10**9
while yo:
    n = up()
    if n == 0: yo ^= yo; continue
    king = go; jester = go
    dummy = [None]*int(n)
    k=0
    while k < len(dummy):
        stuff = list(map(int, __import__("builtins").raw_input().split()))
        i,h,w = stuff
        x = w/(h/1e2)**2-22
        it = x if x >= 0 else -x
        if not (king < it):
            king = it; jester = i
        k+=1
    print(jester)