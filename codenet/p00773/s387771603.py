def tax(p,x):
    return p*(100+x) // 100

def solve(X,Y,S):
    A=0
    sum=0
    NS=0
    for a in range(1,S):
        for b in range(1,S-a+1):
            sum = tax(a,X)+tax(b,X)
            if sum == S:
                NS = tax(a,Y)+tax(b,Y)
                if NS > A:
                    A = NS
            if sum > S:
                break
    return A 

while True:
    X,Y,S = map(int, input().split()) 
    if X == 0:
        break
    print(solve(X,Y,S))