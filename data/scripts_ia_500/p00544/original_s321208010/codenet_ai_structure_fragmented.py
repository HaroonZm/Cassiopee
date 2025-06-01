inf = 10**20

def read_dimensions():
    return map(int, input().split())

def read_flag(n):
    flist = []
    for _ in range(n):
        flag = list(str(input()))
        flist.append(flag)
    return flist

def count_colors(flag):
    w_count = flag.count('W')
    b_count = flag.count('B')
    r_count = flag.count('R')
    return [w_count, b_count, r_count]

def build_wbrnum(flist):
    wbrnum = {}
    for i, flag in enumerate(flist):
        counts = count_colors(flag)
        wbrnum[i] = counts
    return wbrnum

def accumulate_cnti(wbrnum, i):
    cnti = 0
    for l in range(i+1):
        cnti += (wbrnum[l][1] + wbrnum[l][2])
    return cnti

def accumulate_cntj(wbrnum, i, j):
    cntj = 0
    for o in range(i+1, j+1):
        cntj += (wbrnum[o][0] + wbrnum[o][2])
    return cntj

def accumulate_cnto(wbrnum, j, n):
    cnto = 0
    for o in range(j+1, n):
        cnto += (wbrnum[o][0] + wbrnum[o][1])
    return cnto

def main():
    n, m = read_dimensions()
    flist = read_flag(n)
    wbrnum = build_wbrnum(flist)
    cnt = inf
    for i in range(n-2):
        cnti = accumulate_cnti(wbrnum, i)
        for j in range(i+1, n-1):
            cntj = accumulate_cntj(wbrnum, i, j)
            cnto = accumulate_cnto(wbrnum, j, n)
            candidate = cnti + cntj + cnto
            cnt = min(cnt, candidate)
    print(cnt)

main()