N, A, B, C, D = map(int,input().split())
A = A - 1
B = B - 1
C = C - 1
D = D - 1
S = input()
if "##" in S[A:C+1] or "##" in S[B:D+1]:
    print("No")
    exit()

if  D < C and (S[D-1] == "#" or S[D+1] == "#"):
    if "..." in S[B-1:D+1]:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")