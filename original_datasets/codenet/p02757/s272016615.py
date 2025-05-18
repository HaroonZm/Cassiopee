n,p = map(int,input().split())
s = list(map(int, list(input()))) # 数値のリストにしておく

def solve():
    if p in [2,5]: # 例外的な処理
        ret = 0
        for i in range(n): # 文字位置: i: 左から, n-1-i:右から (0 基準)
            lsd = s[n-1-i] # 最下位桁
            if lsd % p == 0: ret += n - i # LSD が割り切れたら LSD から右の桁数分加算
        return ret

    ten = 1 # S[l,r) のときの 10^r, init r=0 -> 10^0 = 1
    cnt = [0]*p # 余りで仕分けして個数を集計
    r = 0 # 左からの文字数 0 のときの余り
    cnt[r] += 1 # 余りが同じものをカウント
    for i in range(n): # 文字位置: i: 左から, n-1-i:右から (0 基準)
        msd = s[n-1-i] # 最上位桁
        r = (msd * ten + r) % p # r: 今回の余り
        ten = ten * 10 % p # N≦2*10^5 桁 なので剰余計算忘れずに！
        cnt[r] += 1 # 余りが同じものをカウント

    ret = 0
    for r in range(p): # 余り r の個数から組み合わせを計算
        ret += cnt[r] * (cnt[r] - 1) // 2 # nCr(n=i,r=2)= n(n-1)/2
    return ret

print(solve())