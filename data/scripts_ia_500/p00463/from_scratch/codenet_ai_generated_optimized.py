import sys
import bisect
input=sys.stdin.readline

while True:
    n,m,h,k=map(int,input().split())
    if n==0 and m==0 and h==0 and k==0:
        break
    s=[int(input()) for _ in range(n)]
    # あみだくじの横棒情報をaで格納。a[i]は縦棒iで横棒がある高さのリスト（ソート済み）
    a=[[] for _ in range(n)]
    horizontal=[]
    for _ in range(m):
        ai,bi=map(int,input().split())
        horizontal.append((ai-1,bi))
        a[ai-1].append(bi)
    for i in range(n):
        a[i].sort()
    # 連続するk本の縦棒を考えるのでインデックスの範囲は0~n-k
    # 関数により、横棒を削除した場合の得点を効率的に計算する
    def score_after_removal(del_idx):
        # del_idx==-1なら削除しない場合
        total=0
        for start in range(n - k + 1):
            # start ~ start+k-1 の縦棒でスコア計算
            res=0
            for i in range(start,start+k):
                # i番の縦棒で最下段に到達する縦棒番号を求める
                pos=i
                # 横棒の影響で入れ替わりが起きるが、それを簡潔に対応する方法は下記
                # 横棒を上端からの距離順(たかさb)にソートすると、あみだくじの経路はbを上から順に通過することで入れ替わりを実行される
                # 横棒を削除しなければ横棒を全て考慮した入れ替わり
                # 削除無しはm本の横棒で両側の縦棒が入れ替わる
                # 削除有は特定の横棒を除いてそこ以外は反映
                # しかし全横棒シミュは高コスト(k*n*m)
                # そこで 横棒の影響は 累積的に考えられるが複雑
                # 解法：
                # 各縦棒について移動後の縦棒番号を管理（逆向きも可）
                # ここではmが最大10万なので全本シミュが可能
                # 最適化のため一回だけ全て適用も良いが削除の差分が欲しい
                # 削除された横棒のみ影響を取り除く（swapしないで済む）
                pass
            # 得点計算時にs[pos]を足す
            pass
        return total

    # 上記は高コストなので異なる方法を使う
    # 解法方針：
    # 横棒は高さ順にソートし、そこから縦棒の入れ替わりを順に行うことで縦棒の現在の配置を得られる
    # 横棒を一本削除するときは、その横棒の削除前後での配置の差分のみ考慮してk本連続部分の得点の最小を求める
    # 実装手順
    # (1) 横棒を高さ順にソートする
    horizontal.sort(key=lambda x:x[1])
    # (2) 横棒無しの状態（初期配置: i番縦棒はi）
    pos=list(range(n))
    # (3) 横棒無しの状態のs配列をposを基に並び替えたものをscoreとする
    score_s=[0]*n
    for i,p in enumerate(pos):
        score_s[i]=s[p]
    # (4) 横棒を通過するとi番縦棒とi+1番縦棒のposを交換する
    # この処理を全て行った結果が現状の配置になる
    for ai,bi in horizontal:
        pos[ai],pos[ai+1]=pos[ai+1],pos[ai]
    # 今posは最終配置を示す
    final_s=[0]*n
    for i,p in enumerate(pos):
        final_s[i]=s[p]
    # 区間和を高速に求めるためのprefix_sum
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+final_s[i]
    # 今、横棒を削除しない得点はk本連続部分の得点の最小値
    ans=10**15
    for start in range(n-k+1):
        ans=min(ans,prefix[start+k]-prefix[start])
    # 横棒iを削除したときの結果を求める
    # 削除すれば横棒iの交換は行われない
    # 削除による配置の差分は、その横棒によるswapを1回キャンセルする形
    # なので、削除した横棒の交換を元に戻せばよい
    # つまり pos配列を、一旦全スワップで作り、その後に一つのswapをキャンセルして区間の得点を計算する
    # この時、全スワップのposは上記final_sを計算済み
    # 削除したスワップの影響を元にするため、
    # final_sは posに対応しているので、
    # 横棒を削除した場合のposは final_posだが、削除した横棒で交換した2要素を再度交換すればよい
    # pos: 現状の縦棒配置=> indexが位置, valueが元縦棒番号
    # swapをキャンセルするとは、 pos[ai],pos[ai+1]の値を再度交換すること
    for idx,(ai,bi) in enumerate(horizontal):
        # コピーしないとpos書換えで破壊するため元に戻す
        tmp=pos[:]
        # 削除横棒のswapをキャンセル
        tmp[ai],tmp[ai+1]=tmp[ai+1],tmp[ai]
        # 新しい配置で得点配列作成
        new_s=[0]*n
        for i,p in enumerate(tmp):
            new_s[i]=s[p]
        # prefix_sum
        prefix2=[0]*(n+1)
        for i in range(n):
            prefix2[i+1]=prefix2[i]+new_s[i]
        # 最小区間和探索
        for start in range(n-k+1):
            val=prefix2[start+k]-prefix2[start]
            if val<ans:
                ans=val
    print(ans)