from __future__ import division,print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass
# 上記のコードはPython2とPython3の違いを一部吸収するためのもの

# def solve(n):
# n : 段数(整数)
# 出力: 一郎君がすべての上り方を実行するのに必要な年数をprintする。
a=[0]*100
def solve(n):
    # ここに問題を解くプログラムをかく。s(4)==s(1)*4+s(2)*2+s(3)*1
    if n==1:
        a[1]=1
        return 1
    elif n==2:
        a[2]=2
        return 2
    elif n==3:
        a[3]=4
        return 4
    elif a[n]!=0:
        return a[n]
    else:
        a[n]=solve(n-3)+solve(n-2)+solve(n-1)
        return a[n]
    

def main():
    while True:
        inp=int(input())
        if inp==0:
            break
        print(solve(inp)//3650+1)

main()