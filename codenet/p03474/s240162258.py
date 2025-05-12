def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

A,B=many_int()

S=one_str()

flg=False
if S[A]=="-":
    temp = S[:A-1] + S[A+1:]
    if temp.isdecimal() and len(S) == A+B+1:
        flg=True

if flg:
    print("Yes")
else:
    print("No")