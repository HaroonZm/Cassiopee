import sys
import collections

input=sys.stdin.readline

def bfs(W,H,X,Y,L,level):
    if level < 1:
        return 0
    visited = [[False]*W for _ in range(H)]
    q = collections.deque()
    if L[Y-1][X-1] <= level:
        q.append((X-1,Y-1))
        visited[Y-1][X-1]=True
    count=0
    while q:
        x,y=q.popleft()
        count+=1
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny=x+dx,y+dy
            if 0<=nx<W and 0<=ny<H and not visited[ny][nx] and L[ny][nx]<=level:
                visited[ny][nx]=True
                q.append((nx,ny))
    return count

while True:
    R=int(input())
    if R==0:
        break
    W1,H1,X1,Y1=map(int,input().split())
    L1=[list(map(int,input().split())) for _ in range(H1)]
    W2,H2,X2,Y2=map(int,input().split())
    L2=[list(map(int,input().split())) for _ in range(H2)]

    # 部屋の最大機密レベルの範囲探索
    maxL1 = max(max(row) for row in L1)
    maxL2 = max(max(row) for row in L2)

    # 事務所1で認証レベルl1なら訪問可能部屋数
    def reachable1(l1):
        return bfs(W1,H1,X1,Y1,L1,l1)
    # 事務所2で認証レベルl2なら訪問可能部屋数
    def reachable2(l2):
        return bfs(W2,H2,X2,Y2,L2,l2)

    # 全組み合わせ走査は不可なので認証レベルの和の最小値を求めるため二分探索
    # 認証レベルは0以上、最大はmaxL1+maxL2と見積もる
    low,high=0,maxL1+maxL2
    ans=10**15
    while low <= high:
        mid=(low+high)//2
        # このmid以下の合計認証レベルでR以上の部屋数が可能か判定
        # iを事務所1側の認証レベル、mid - iを事務所2側の認証レベルとするときの最大訪問部屋数を確認
        possible=False
        start = max(0, mid - maxL2)
        end = min(mid, maxL1)
        # 二分探索高速化のため，認証レベルは逐次取得，最後m1部屋数,m2部屋数を調べて足してR以上か判定
        # BFS重いため全探索は不可. 方針を変えて，認証レベルの閾値により部屋数は単調増加であることから，
        # それぞれの事務所について認証レベルと訪問可能部屋数のペアを先に取得してから探索する。
        # 事務所1と2の認証レベルを全域に渡り計算しなおすのは計算量的に厳しいため、
        # 認証レベルを0からmaxLの範囲で二分探索して訪問可能部屋数の関数を得る（もしくは一回の二分探索で）
        # ここではそれぞれ単一事務所で可能な訪問部屋数が単調増加であることを利用し、各社について必要に応じて二分探索する。

        # 事務所1の認証レベルの最低は0,最高はmaxL1
        # mid - l1 = l2
        # l1 ∈ [start,end]
        # 対応するl2 = mid - l1

        # 訪問部屋数は単調増加なので，それぞれの事務所の認証レベルごとの最大到達部屋数をキャッシュする
        # キャッシュなし:とりあえず全てのl1を試すとTLEなので，事務所1の複数l1を二分探索に置き換えたい
        # 考え方を変えた:
        # 事務所1の最大訪問部屋数はmaxn1 = W1*H1
        # 事務所2の最大訪問部屋数はmaxn2 = W2*H2
        # R <= maxn1+maxn2

        # 認証レベルの最大値は10^8未満で大きい
        # 閾値だけでbfs実行するよりも高速化必要．
        # よって各事務所の機密レベルの部屋をリスト化し，levelの閾値以下の部屋をグラフから訪問を調べるため、
        # BFS内の条件は L[v]<=level
        # 探索ごとにO(W*H)
        # levelの種類は多いが唯一昇順に並べる方法と二分探索を組み合わせて高速化。

        break

    # → 上記方針は重く実装的に難しいため以下の手法を実装する。
    # 方針：
    # 各事務所について、機密レベル群を昇順にソートし、ユニークにする。
    # 2分探索により各事務所の認証レベル候補を決める
    # 各候補認証レベルで可能な訪問部屋数をBFSで計算する
    # 全体として認証レベルの和について二分探索を行う
    # 各midについて認証レベル1と認証レベル2の候補はそれぞれ0からmidまでで、それらを順に試すことで判定
    # 実装は時間ギリギリのため、各事務所の機密レベルのリストを作り、認証レベルの二分探索→訪問部屋数計算
    # 事務所の認証レベルは0も含めて候補。0なら入れない。1以上ならホールは必ず入れる。

    # 事務所1の候補レベル列作成
    levels1 = sorted(set([0]+[val for row in L1 for val in row]))
    levels2 = sorted(set([0]+[val for row in L2 for val in row]))

    from bisect import bisect_right

    def max_reachable(levels,L,W,H,X,Y,level):
        # BFSで訪問可能部屋数を計算
        # 入力のレベルは候補値であり、Lの部屋レベルと比較し
        # この関数は呼ばれる時、0含め有効値であると期待
        return bfs(W,H,X,Y,L,level)

    # 事務所それぞれの訪問可能部屋数を求める関数: 認証レベルから訪問部屋数（二分探索結果）
    def reachable_func(levels,L,W,H,X,Y):
        cache={}
        def f(level):
            if level in cache:
                return cache[level]
            res = bfs(W,H,X,Y,L,level)
            cache[level]=res
            return res
        return f

    f1=reachable_func(levels1,L1,W1,H1,X1,Y1)
    f2=reachable_func(levels2,L2,W2,H2,X2,Y2)

    low,high = 0,levels1[-1]+levels2[-1]
    ans=10**15

    # 認証レベルは候補が離散的なため、low, highは整数でよい。
    # また0も含む。
    while low <= high:
        mid=(low+high)//2
        possible=False
        # 事務所1の認証レベルiを0..midで試す
        # 認証レベルはlevels1とlevels2に離散化されているので、
        # levels1の候補値でi<=midを満たす最大の認証レベル
        # levels2の認証レベルはmid - i

        # 事務所1の認証レベルの候補を絞る
        l1_candidates = [level for level in levels1 if level <= mid]
        for l1 in l1_candidates:
            l2 = mid - l1
            # l2は 0 <= l2 <= max possible 認証レベル
            # levels2から l2 以下の最大値を取得
            pos2 = bisect_right(levels2,l2)
            if pos2 ==0:
                l2_cand = 0
            else:
                l2_cand = levels2[pos2-1]
            c1 = f1(l1)
            c2 = f2(l2_cand)
            if c1+c2 >= R:
                possible=True
                break
        if possible:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    print(ans)