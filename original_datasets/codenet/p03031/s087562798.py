from collections import Counter

def solve(n, m, sx, p):
    ans = 0
    temp_c_list = []
    for i in range(1 << (n)):
        for si in sx:
            sum_si = sum(si)
            c = Counter(bin(i & sum_si)[2:])['1']
            temp_c_list.append(c % 2)
        if px == temp_c_list:
            ans += 1
        temp_c_list = []

    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    sx = [[0]*n for _ in range(m)]

    for i in range(m):
        tx = list(map(int, input().split()))[1:]
        for ti in tx:
            sx[i][n-ti] = 1 << ti-1

    px = list(map(int, input().split()))

    print(solve(n, m, sx, px))