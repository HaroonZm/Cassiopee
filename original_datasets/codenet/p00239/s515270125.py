"""
Calorie Counting
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0239

"""
import sys

def solve(foods, limit):
    ans = []
    for s, p, q, r in foods:
        total_calorie = p*4 + q*9 + r*4
        if all([x <= y for x, y in zip([p, q, r, total_calorie], limit)]):
            ans.append(s)
    return ans if ans else ['NA']

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        foods = [list(map(int, input().split())) for _ in range(n)]
        limit = list(map(int, input().split()))
        ans = solve(foods, limit)
        print(*ans, sep='\n')

if __name__ == '__main__':
    main(sys.argv[1:])