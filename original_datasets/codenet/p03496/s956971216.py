import io
import sys
import math

# 0 - 2N回まで実行できる
def add_x_to_y():
    pass

def is_condition_ok(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def check_plus_minus(lst):
    # 戻り値：
    # 正の値のみ：1, 負の値のみ：-1, 正負混在：0
    p_flag = False
    m_flag = False
    for a in lst:
        if a >= 0:
            p_flag = True
        else:
            m_flag = True
        if p_flag and m_flag:
            return 0
    return 1 if p_flag else -1

# 経路が発見出来たら出力を整形する。
def format_multi_answer(lst):
    ans = ""
    ans += f"{len(lst)}\n"
    for y in lst:
        ans += f"{y[0]} {y[1]}\n"
    return ans

def solve(n,a_lst):
    """
    戦略A：
    [全て正の場合]
    ・左から、NGとなる値のiを得る。
    ・その値に正の値を足し込む
    　・リスト中、最大の正の値を足し込む
    　　・iの値が最大となる
    　・以後、右の値を全て更新する。最大でN-1回のオペレーションになる。
    [全て負の場合]
    ・同様に、右から探査し、最小の負の数を更新していく。最大でN-1回のオペレーションになる。
    [正負混在する場合]
    ・最大値/最小値を取る。
    ・正負いずれかに揃える。（絶対値の大きい側に、全ての値を揃える）（最大でN-1回）
    ・上記の正負処理をする。（最大でN-1回）
    """
    # implement process
    if is_condition_ok(a_lst):
        return 0

    plus_minus = check_plus_minus(a_lst)

    ans_lst = []
    if plus_minus == 1:
        y = 0
        for i in range(len(a_lst)-1):
            if a_lst[i] > a_lst[i+1]:
                y = i+1
                break
        x = -1
        a_max = -1
        for i in range(len(a_lst)):
            if a_max < a_lst[i]:
                a_max = a_lst[i]
                x = i
        ans_lst.append([x+1,y+1])
        for i in range(y, len(a_lst)-1):
            ans_lst.append([i+1,i+2])
    
    elif plus_minus == -1:
        y = 0
        for i in range(len(a_lst)-1,0,-1):
            if a_lst[i] < a_lst[i-1]:
                y = i-1
                break
        x = +1
        a_min = +1
        for i in range(len(a_lst)):
            if a_min > a_lst[i]:
                a_min = a_lst[i]
                x = i
        ans_lst.append([x+1,y+1])
        for i in range(y,0,-1):
            ans_lst.append([i+1,i])
    
    elif plus_minus == 0:
        # get max / min value and index
        i_max, a_max = -1,-1
        i_min, a_min = +1,+1
        for i in range(len(a_lst)):
            if a_max < a_lst[i]:
                a_max = a_lst[i]
                i_max = i
            if a_min > a_lst[i]:
                a_min = a_lst[i]
                i_min = i

        if a_max > abs(a_min):
            # まず、全ての負の値にmax値を足し込み、正の値にする。
            # 次に、plus時の処理を行う。
            for i in range(len(a_lst)):
                if a_lst[i] < 0:
                    a_lst[i] += a_max
                    ans_lst.append([i_max+1,i+1])
            if _DEB: logd(f"lst: {a_lst}")

            y = -1
            for i in range(len(a_lst)-1):
                if a_lst[i] > a_lst[i+1]:
                    y = i+1
                    break
            if y != -1:
                ans_lst.append([i_max+1,y+1])
                for i in range(y, len(a_lst)-1):
                    ans_lst.append([i+1,i+2])
        else:
            # 全ての正の値を負の値にし、minus時の処理を行う。
            for i in range(len(a_lst)):
                if a_lst[i] >= 0:
                    a_lst[i] += a_min
                    ans_lst.append([i_min+1,i+1])
            if _DEB: logd(f"lst: {a_lst}")

            y = -1
            for i in range(len(a_lst)-1,0,-1):
                if a_lst[i] < a_lst[i-1]:
                    y = i-1
                    break
            if y != -1: 
                ans_lst.append([i_min+1,y+1])
                for i in range(y,0,-1):
                    ans_lst.append([i+1,i])

    return format_multi_answer(ans_lst)

def main():
    # input
    n = int(input())
    a_lst = list(map(int, input().split()))

    # process
    if _DEB: logd(f"a_lst: {a_lst}") 
    ans = str( solve(n,a_lst) ).strip()
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
2
-1 -3
"""
_EXPECTED = """\
2
2 3
3 3
"""

def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB: print(f"[deb] {str}")

### MAIN ###
if __name__ == "__main__":
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Debug Mode !!")

    ans = main()

    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip(): print("!! Success !!")
        else: print(f"!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}")