N,A,B,C,D = map(int, input().split())
# Pour être sûr qu'on bosse à partir de 0
A = A-1
B = B-1
C = C-1
D = D-1
S = input()
# Check rapide: s'il y a double # c'est mort
if '##' in S[A:C+1] or '##' in S[B:D+1]:
    print('No')
    exit()
# Le cas où B doit dépasser C (un peu tricky)
if D < C:
    # Faut un espace pour doubler quelqu'un...
    if S[D-1] == "#" or S[D+1] == "#":
        if "..." in S[B-1:D+2]:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')
else:
    print('Yes')