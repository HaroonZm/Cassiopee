"""
Problem A: 次期町長
https://onlinejudge.u-aizu.ac.jp/problems/1159
2≤ N ≤10000、1≤ K ≤10000、1≤ M ≤ Nß
"""
def solve(n, k, m):

    table = [i+1 for i in range(n)]
    taget = m-1
    while(len(table)>1):

        table.pop(taget)
        taget -= 1
        taget = (taget+k)%len(table)

    return table[0]

if __name__ == '__main__':
    ans = []
    while(True):
        n, k, m = map(int, input().split())
        if n == 0 and k == 0 and m == 0:
            break
        ans.append(solve(n, k, m))
    print(*ans, sep='\n')