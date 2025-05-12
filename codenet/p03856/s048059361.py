S=input().strip()
def solve(S):
    while len(S)>0:
        if S[-6:]=='eraser':
            S=S[:-6]
        elif S[-7:]=='dreamer':
            S=S[:-7]
        elif S[-5:]=='erase':
            S=S[:-5]
        elif S[-5:]=='dream':
            S=S[:-5]
        else:
            return False
    return True

if solve(S):
    print('YES')
else:
    print('NO')