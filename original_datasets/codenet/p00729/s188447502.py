def main():
    ans_list = []

    while True:
        ans = solve()
        if ans == -1:
            break
        ans_list += ans

    for ans in ans_list:
        print(ans)

def solve():
    res_list = []
    N,M = map(int,input().split())
    if (N,M) == (0,0):
        return -1
    sh = [[0]*(1260-540+1) for _ in range(M)]
    r = int(input())
    for _ in range(r):
        t,n,m,s = map(int,input().split())
        t -= 540
        m -= 1
        if s == 1:
            sh[m][t] += 1
        elif s == 0:
            sh[m][t] -= 1
    acc = 0
    for i,line in enumerate(sh):
        for j,bit in enumerate(line):
            acc += bit
            if acc >= 1:
                sh[i][j] = 1
            else:
                sh[i][j] = 0
    q = int(input())
    for _ in range(q):
        ts,te,m = map(int,input().split())
        ts -= 540
        te -= 540
        m -= 1
        res = sum(sh[m][ts:te])
        res_list.append(res)
    return res_list
    
main()