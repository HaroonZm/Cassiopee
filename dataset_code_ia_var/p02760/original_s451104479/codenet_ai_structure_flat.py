import sys
A0 = list(map(int, input().split()))
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
N = int(input())
b = []
for _ in range(N):
    b.append(int(input()))
ans00 = False
ans01 = False
ans02 = False
ans10 = False
ans11 = False
ans12 = False
ans20 = False
ans21 = False
ans22 = False
if A0[0] in b:
    ans00 = True
if A0[1] in b:
    ans01 = True
if A0[2] in b:
    ans02 = True
if A1[0] in b:
    ans10 = True
if A1[1] in b:
    ans11 = True
if A1[2] in b:
    ans12 = True
if A2[0] in b:
    ans20 = True
if A2[1] in b:
    ans21 = True
if A2[2] in b:
    ans22 = True
if ans00 and ans10 and ans20:
    print('Yes')
    sys.exit()
if ans01 and ans11 and ans21:
    print('Yes')
    sys.exit()
if ans02 and ans12 and ans22:
    print('Yes')
    sys.exit()
if ans00 and ans01 and ans02:
    print('Yes')
    sys.exit()
if ans10 and ans11 and ans12:
    print('Yes')
    sys.exit()
if ans20 and ans21 and ans22:
    print('Yes')
    sys.exit()
ans_flag = True
ans_flag2 = True
if not ans00:
    ans_flag = False
if not ans11:
    ans_flag = False
if not ans22:
    ans_flag = False
if not ans02:
    ans_flag2 = False
if not ans11:
    ans_flag2 = False
if not ans20:
    ans_flag2 = False
if ans_flag or ans_flag2:
    print('Yes')
else:
    print('No')