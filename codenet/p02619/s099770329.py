from bisect import bisect_left

class score:
    def __init__(self,t) -> None:
        self.t = t
        score = 0
        last = [[] for i in range(26)]
        for i,ti in enumerate(t):
            score += s[i][ti-1]
            last[ti-1].append(i+1)
            for tj in range(26):
                if last[tj-1] == []:
                    score -= c[tj-1]*(i+1)
                else:
                    #print(last)
                    score -= c[tj-1]*((i+1)-last[tj-1][-1])
            print(score)
        self.score = score
    def a__init__(self,t) -> None:
        score = 0
        last = [[] for i in range(26)]
        for i,ti in enumerate(t):
            # 開催分を加算
            score += s[i][ti-1]
            # 減らす
            if last[ti-1] == []:
                score -= c[i]*i+1
            else:
                score -= c[i]*((i+1)-last[ti-1][-1])
            last[ti-1].append(i+1)
            print(score)
        for i in range(26):
            if last[i] == []:
                score -= c[i]*D
            else:
                score -= c[i]*(D-last[i][-1])
        self.score = score
        self.t = t

D = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for i in range(D)]
t = [int(input()) for i in range(D)]

sc = score(t)
#print(sc.score)