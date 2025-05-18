"""
Problem A: ICPC 得点集計ソフトウェア
"""
if __name__ == '__main__':
    ans = []
    while(True):
        n = int(input())
        if n == 0:
            break
            
        l = [int(input()) for _ in range(n)]
        maxi = max(l)
        mini = min(l)
        ans.append((sum(l) - maxi - mini)//(n-2))
    print(*ans, sep='\n')