"""
Writer: SPD_9X2
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_B&lang=ja

各セルに対して、上にいくつ0が連続しているか数えれば、
ヒストグラム上での最大長方形問題になる
"""

def Largest_rectangle_in_histgram(lis):

    stk = []

    ans = 0
    N = len(lis)

    for i in range(N):

        if len(stk) == 0:
            stk.append((lis[i],i))

        elif stk[-1][0] < lis[i]:
            stk.append((lis[i],i))

        elif stk[-1][0] == lis[i]:
            pass

        else:
            lastpos = None
            while len(stk) > 0 and stk[-1][0] > lis[i]:

                nh,np = stk[-1]
                lastpos = np
                del stk[-1]

                ans = max(ans , nh*(i-np))

            stk.append((lis[i] , lastpos))

    return ans

H,W = map(int,input().split())

c = []
for i in range(H):
    C = list(map(int,input().split()))
    c.append(C)

zlis = [ [0] * (W+1) for i in range(H) ]
for i in range(H):
    for j in range(W):

        if c[i][j] == 1:
            continue
        elif i == 0:
            zlis[i][j] = 1
        else:
            zlis[i][j] = zlis[i-1][j] + 1

#print (zlis)
ans = 0
for i in range(H):
    ans = max(ans , Largest_rectangle_in_histgram(zlis[i]))

print (ans)