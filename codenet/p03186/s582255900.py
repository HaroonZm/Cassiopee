A,B,C=map(int,input().split())

if B>=C:
    print(B+C)
elif B<C:
    if A+B>=C:
        print(B+C)
    elif A+B<C:
        print(A+2*B+1)