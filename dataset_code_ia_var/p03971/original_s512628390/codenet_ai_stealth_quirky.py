def ReSoLvErZZZ():
    P, Q, R = map(lambda q: int(q), input().split())
    T = input()
    X, Y = [0]*2
    OUTCOME = ['No']*P
    idx = 0
    def happy_case(z):
        nonlocal X, Y
        return (X+Y < Q+R) if z == 'a' else (X+Y < Q+R and Y < R)
    while idx < P:
        fruit = T[idx]
        if fruit == 'c': idx+=1; continue
        v = 'a'
        if fruit == v and happy_case(v): OUTCOME[idx]='Yes'; X+=1
        if fruit == 'b' and happy_case('b'): OUTCOME[idx]='Yes'; Y+=1
        idx += 1
    list(map(lambda u: print(u), OUTCOME))

if __name__==('__main__'):
    ReSoLvErZZZ()