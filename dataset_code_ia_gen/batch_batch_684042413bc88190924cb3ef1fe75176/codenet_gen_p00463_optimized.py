import sys
input=sys.stdin.readline

while True:
    n,m,h,k=map(int,input().split())
    if n==0 and m==0 and h==0 and k==0:
        break
    s=[int(input()) for _ in range(n)]
    ladders=[[] for _ in range(h)]
    for _ in range(m):
        a,b=map(int,input().split())
        ladders[b-1].append(a-1)

    # 位置iの縦棒配置を表す配列。初期は[i,i+1,...] 縦棒のインデックスを示す
    position=list(range(n))
    # 横棒の位置ごとに順番を更新（横棒は高さbで縦棒aとa+1を結ぶ）
    # 下から上に向かって経路をたどるため高さが小さい順に処理
    # ここではsは下端の点数、縦棒の初期位置は0~n-1
    
    # 横棒の高さ升でソート済み,小さい順に処理
    # 横棒iで縦棒iとi+1をswapする
    for height in range(h):
        for a in sorted(ladders[height]):
            position[a],position[a+1]=position[a+1],position[a]

    # 位置pos[i]は縦棒iの下端の位置。pos[i]=jなら縦棒iはj番目の下端につながる
    pos=[0]*n
    for i,p in enumerate(position):
        pos[p]=i

    # prefix sumで区間和高速取得
    pref=[0]*(n+1)
    for i in range(n):
        pref[i+1]=pref[i]+s[pos[i]]

    # 変更なしのスコア最小のk連続区間
    ans=min(pref[i+k]-pref[i] for i in range(n-k+1))

    # 各横棒を削除した場合を考える
    # 横棒を削除すると、該当位置のswapが一つ消えるので、一度swapをしていた部分を元に戻す
    # だがmが最大10万かつnは最大1000なので、それぞれの横棒について全換算は大きすぎる
    # 最適化として：
    # 初期配置は1->pos[1], 2->pos[2]　→初期状態のpos配列
    # 横棒一つを削除すると、その横棒のswapが消え、
    # つまりその位置の高さのswapが一つなくなる。
    # 横棒は高さbでa,a+1がswapしていたがこれは降順処理で何回もswapしているので一つ削除により差分を調査
    
    # 逆変換：pos[i]=j　は、縦棒iがj番目に対応
    # 実はこのあみだくじの経路は高さの低い順にswapしていけば最後にposができる
    # 削除での補正はそのswapを一回消すこと
    # 削除したらposはどのように変わるかを計算する
    # swap消去は、swapのあった高さのa,a+1を逆にswapし直すことに相当
    
    # そこで、初期のswap操作を配列で持ち、位置毎の配列を初期生成し、
    # 1つの横棒を削除した場合は、そのswapの反対処理を行いposを調整する
    # そして、k連続区間の和を計算して最小値更新
    
    # 高さごとにswapを集めていたが、
    # 横棒情報をm本リストを保持し、高さごとの種類も覚えている
    
    # 実装：
    # 1.pos配列は完成
    # 2.初期stateの逆マップ逆_pos（位置から縦棒）も作成
    # 3.各横棒を削除すると、swapで元に戻す。つまりposの方に逆swapを施す
    # 4.posの変更は小さい範囲のみなのでO(1)で可能
    # 5.変更後のpos配列を使いスコア計算（s[pos[i]]を連続で足すのがO(n)だがn=1000ならm=10万でも回せる）
    # 6.さらに高速化のためpref配列を毎回作るのは重いがn=1000で最大10回程度なので許容範囲
    
    # 横棒情報をまとめた配列 original_swaps: (height,a) と順番を記憶
    original_swaps=[]
    for height in range(h):
        for a in ladders[height]:
            original_swaps.append((height,a))
    # 横棒の入力順にマッピングがわからないので入力順に並び変え直す
    # 入力順でm本情報はあるが高さはb_i-1、a_i-1
    # 入力順でswapを配列化
    ladder_list=[]
    for b_i in range(m):
        # 入力は未保存なので再読み込み不可、再読み込み対策として42行目等に変数で保存
        pass
    # よって入力のm行は別に保存しておき再利用
    
    # 再提出案：
    # 入力の横棒はm本の(a_i,b_i)で入手するので、それでm本リストを保存する
    # それぞれ削除時にswapを戻す処理を行う
    
    import bisect

    sys.stdin.seek(0)
    lines=sys.stdin.read().splitlines()
    p=0
    while True:
        n,m,h,k=map(int,lines[p].split())
        p+=1
        if n==0 and m==0 and h==0 and k==0:
            break
        s=list(map(int,lines[p:p+n]))
        p+=n
        ladders_input=[tuple(map(int,lines[p+i].split())) for i in range(m)]
        p+=m

        ladders=[[] for _ in range(h)]
        for i,(a,b) in enumerate(ladders_input):
            ladders[b-1].append((a-1,i))

        # 全横棒を高さ順にソート
        all_swaps=[]
        for height in range(h):
            for a,i_lad in sorted(ladders[height]):
                all_swaps.append((height,a,i_lad))

        # 最終配置作成
        position=list(range(n))
        for _,a,_ in all_swaps:
            position[a],position[a+1]=position[a+1],position[a]

        pos=[0]*n
        for i,p_ in enumerate(position):
            pos[p_]=i

        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+s[pos[i]]
        ans=min(pref[i+k]-pref[i] for i in range(n-k+1))

        # posと逆posを作成
        # pos[i]:縦棒iの下端位置
        # inv_pos[j]:下端位置jにある縦棒
        inv_pos=[0]*n
        for i,v in enumerate(pos):
            inv_pos[v]=i

        # 横棒削除時の影響処理関数
        def calc_after_removal(rm_i):
            # rm_i番目の横棒を削除。all_swapsは昇順に並んでいる。
            # 削除した横棒のswap(a,a+1)を逆swapで元に戻す
            # まずそのswapが何かを得る
            height,a,idx=all_swaps[rm_i]
            # 元のpos,inv_posからswap逆にやる
            # j = pos[a], j+1 = pos[a+1]
            # 今pos[a]とpos[a+1]の値はswap済みの最終配置なので、下端の位置は
            # 垂直棒aはpos[a]で位置があるがswap逆したら位置が元に戻る
            # posをコピー
            pos2=pos[:]
            inv_pos2=inv_pos[:]
            x=pos2[a]
            y=pos2[a+1]
            # swap逆すれば下端位置x,yの縦棒はそれぞれ入れ替わる
            pos2[a],pos2[a+1]=y,x
            inv_pos2[x],inv_pos2[y]=a+1,a
            # s[pos2[i]]の配列作成
            arr=[0]*n
            for i in range(n):
                arr[i]=s[pos2[i]]
            pref2=[0]*(n+1)
            for i in range(n):
                pref2[i+1]=pref2[i]+arr[i]
            return min(pref2[i+k]-pref2[i] for i in range(n-k+1))

        # 削除しない場合も考慮済みなので
        # 各横棒について削除時の得点を計算しans更新
        for rm_i in range(len(all_swaps)):
            val=calc_after_removal(rm_i)
            if val<ans:
                ans=val
        print(ans)