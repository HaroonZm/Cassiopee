import itertools
import math

N,A,B = list(map(int,input().split(" ")))
hs = [int(input()) for _ in range(N)]

OK = 10 ** 10 #この以上回数やればOK
NG = 0  # この回数以下だとNG

while OK - NG > 1:
    target = (OK + NG) // 2 #  今回試される数字
    s = 0 # 合計s回魔法が使われる
    for h in hs:
        temp = (h- target * B)/(A-B)
        temp = math.ceil(temp)
        s += max(temp,0)
    if target >= s:
        OK = target
    else:
        NG = target
print(OK)