import sys

def query(num):
    print("?", num)
    sys.stdout.flush()
    res = input()
    return res

"""
def query(num):
    print(num)
    if num == "":
        num = "0"
    if int(num) <= N and num <= str(N):
        return "Y"
    if int(num) > N and num > str(N):
        return "Y"
    return "N"
"""

def solve():
    ans = ""
    while len(ans) < 20:
        if len(ans) == 0:
            min_lim = 1
        else:
            min_lim = 0
        ok = 10
        ng = min_lim
        if query((ans + str(min_lim) + 9 * "9")[:17]) == "Y":
            if query(ans + "2") == "N":
                ans += str(min_lim)
                continue
            if query("1" + len(ans) * "0") == "Y":
                ans += str(min_lim)
                print("!", ans)
                return
            else:
                print("!", ans)
                return
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if query((ans + str(mid) + 9 * "9")[:17]) == "Y":
                ok = mid
            else:
                ng = mid
        ans += str(abs(ok))

N = 1000000000
solve()