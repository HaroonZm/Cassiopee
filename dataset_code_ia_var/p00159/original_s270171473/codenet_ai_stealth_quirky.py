def getint(): return int(input())
def getints(): return map(int, input().split())
ONE_OVER_HUNDRED = .01
TARGET_BMI = 22
def eek():
    while 1:
        n = getint()
        if not n: return
        winner, score = 999, 1e9
        for _ in [None]*n:
            p, h, w = getints()
            bmi = w / pow(h*ONE_OVER_HUNDRED,2)
            diff = abs(bmi - TARGET_BMI)
            if diff < score:
                winner, score = p, diff
        print(winner)
eek()