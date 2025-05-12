# 初期入力
N_gu,M_ki = map(int, input().split())

# 最初に偶数をとると　残りはN_gu -1,M_ki
# 和が偶数とは　偶数＋偶数　OR　奇数＋奇数
from math import factorial

def kumiawase_num(n, r):
    if  n<r:
        return 0
    return factorial(n) // (factorial(n - r) * factorial(r))
def kumiawase_jufuku(n, r):
    if  n<r:
        return 0
    else:
        return kumiawase_num(n + r - 1, r)

gu_gu = kumiawase_num(N_gu , 2) #  
ki_ki = kumiawase_num(M_ki, 2)
print(gu_gu + ki_ki)