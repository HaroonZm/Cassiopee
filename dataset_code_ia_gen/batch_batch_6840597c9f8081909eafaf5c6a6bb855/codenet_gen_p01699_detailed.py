# 解法アプローチ：
# 各エレベーターiは low_iから high_i までの階数に止まることができる。  
# 各エレベーターの可能な階数の数を掛け合わせれば、全組み合わせの数が得られる。  
# 例えば、N=3で、エレベーターの範囲がそれぞれ [10,10], [2,2], [11,11] の場合は、  
# 各々1通りなので組み合わせは1 * 1 * 1 = 1。  
# また、計算結果は非常に大きくなる可能性があるため、int型(Pythonでは自動的に大きい数も扱える)で問題なし。  
# 入力を複数処理し、終了条件は1行に0のみが書かれていること。  

def main():
    import sys
    input = sys.stdin.readline
    
    while True:
        line = input().strip()
        if line == '0':  # 終了条件
            break
        N = int(line)
        ranges = []
        for _ in range(N):
            low, high = map(int, input().split())
            ranges.append((low, high))
        # 組み合わせ数を計算
        total = 1
        for low, high in ranges:
            total *= (high - low + 1)
        print(total)

if __name__ == "__main__":
    main()