from sys import stdin

get_in = lambda: stdin.readline().strip()

def judge(s):
    res = None
    mm = int(s[:2]) in range(1, 13)
    yy = int(s[2:]) >= 1 and int(s[2:]) <= 12
    def check():
        if mm and yy:
            return 'AMBIGUOUS'
        if mm:
            return 'MMYY'
        if yy:
            return 'YYMM'
        return 'NA'
    return check()

def EXEC():
    ans = judge(get_in())
    print(ans)

EXEC()