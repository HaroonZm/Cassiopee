while True:
    r,c,q = map(int,input().split())
    if r==0 and c==0 and q==0:
        break
    # 最後に指示があった行と列を記録
    last_row = [-1]*(r)
    last_col = [-1]*(c)
    for i in range(q):
        A,B,order = map(int,input().split())
        if A==0:
            last_row[B] = i
        else:
            last_col[B] = i
    # 起立している座席を特定
    # 最後に指示された回数が大きい順に判定し、被らないようにカウント
    visited_row = [False]*r
    visited_col = [False]*c
    res=0
    # 指示はq回なのでq-1→0の順に処理すると先に大きい番号が処理される
    for i in range(q-1,-1,-1):
        # 該当する行を起立にしている指示なら
        for idx in range(r):
            if last_row[idx]==i:
                # orderは判明していないので判定を入れる
                # しかしorderがわからないのでここは後回しにする
                # 問題文からorderは入力とセットなので入力時に使いたい
                pass
        for idx in range(c):
            if last_col[idx]==i:
                pass
    # 上記はすこし複雑なので、別のやり方を試す
    # 実は最後の指示だけが効くので記録し、行と列の指示をq回分で記録しておく

    # 行、列ごとの最後の指示indexと指示内容を別に保存
    last_row_order = [-1]*r
    last_col_order = [-1]*c
    input_pos = 0
    # 再度入力取りなおしはできないので、一回で処理しよう

    # なので最初にq回の指示を受け取って保存する実装に変える
    # このため、おもな処理を関数化しよう。初心者っぽくはないが。

# 関数の先に再度全コードをまとめて初心者っぽいシンプルな方法で書きなおす

def main():
    while True:
        r,c,q = map(int,input().split())
        if r==0 and c==0 and q==0:
            break
        last_row_order = [-1]*r
        last_col_order = [-1]*c
        last_row_command = [-1]*r
        last_col_command = [-1]*c
        for i in range(q):
            A,B,order = map(int,input().split())
            if A==0:
                last_row_order[B] = i
                last_row_command[B] = order
            else:
                last_col_order[B] = i
                last_col_command[B] = order
        res = 0
        counted_rows = [False]*r
        counted_cols = [False]*c
        # q回中、最後に指示が大きい順から処理していく
        # 大きい番号から小さい番号に並べ替えは指示と合わせて難しいから、
        # 単純にrとcそれぞれのインデックス分調べるだけで十分
        # 各行・列で最大の指示番号を比較し、未カウントなら起立ならカウント
        # ただし被ったら加算しない → 最悪の場合なので被る箇所は重複させない
        # ここでのポイントは、行指示と列指示が競合する座席は被るので最終的に起立になるか否か判断がいる

        # なので参加席数はr*cでかなり多いので全席調べるのは無理
        # 簡単に考えると、起立する席は「行全部が立つ指示」または「列全部が立つ指示」が最後の指示で立っている状態の人
        # 行列のうち最も新しい指示番号が効く
        # 各行の最後の指示の番号と内容
        # 各列の最後の指示の番号と内容
        # 例えば座席(i,j)に対して最後に指示されたのは最後に行iか列jのどちらかで指示があったほうが新しい
        # その指示の内容が1なら起立、0なら着席
        # 最後に起立の人だけが入場できる

        # 集計簡単にするために、この事実だけ使う

        # なので行iの最後の指示番号と命令orderRow
        # 列jの最後の指示番号と命令orderCol

        # 座席(i,j)は最後に指示された回数 max(last_row_order[i], last_col_order[j]) の方の order が最終状態

        # 起立の座席の数 = { (i,j) | 最終状態1 }

        # 最悪の場合に入場できる数はその数

        # しかしr,cが最大5万でr*cは最大2500000000で全座席調べるのは impossible

        # なので逆に起立している座席の総数を効率的に計算する方法を考える

        # 行ごとに最後の指示が行だった場合、行のすべての座席はその指示のorderになる
        # 同様に列ごとに最後の指示が列だった場合、その列の座席はその指示のorderになる

        # 座席(i,j)に対して
        #   row_t = last_row_order[i]
        #   col_t = last_col_order[j]
        #   if row_t > col_t:
        #       最終状態 = last_row_command[i]
        #   else:
        #       最終状態 = last_col_command[j]

        # 注: row_tやcol_t が-1 は指示なしの状態
        # -1 は指示がないなら基本は最初は座ってると思う（起立してない）

        # 探す対象は起立している座席数 => これが人数
        # この数が最悪の場合何番目までに到着すれば入場できる人数

        # 実際にはbrute force無理なので少し工夫

        # どの座席でも最終状態の計算は (row_t,col_t)の大小比較だけ

        # row_tとcol_tは-1もあり得るので、-1は十分小さく扱う（指示がない）

        # 行が-1, 列が指示ありなら座席の状態は列の指示

        # 行と列の指示状態をそれぞれ分け、同じ指示時間は同列に合わせてほぼないため

        # 実装

        # 行ごとにラベル代入
        # 行 -> (last指示時間, 最後の命令)
        # 同様列

        # まず、各行の最後の指示がなければ(-1,0)座ってるとみなす
        for i in range(r):
            if last_row_order[i]==-1:
                last_row_order[i] = -1
                last_row_command[i] = 0
        for j in range(c):
            if last_col_order[j]==-1:
                last_col_order[j] = -1
                last_col_command[j] = 0
        # 行座標の配列と列座標の配列を作る(これらは長い)
        # 各行の指示時刻でソートしておく（未使用かも）

        # 起立者数を数える方法は
        # 起立している座席の数を数えるには、
        # 起立している行 seats = 行が最後に起立の場合は全c席カウント
        # ただし、列が最後に立った場合は列が優先

        # つまり各行で最後の指示が行のとき、その行の座席は orderRow[i] になるが
        # その座席の最終状態を決めるには、その列の指示時刻との比較がいる

        # これにより、最後の指示で列の方が新しいなら、その列のorderが優先される

        # 処理の概要は
        # 1 行が最後に指示された座席は最後に列が指示された座席で覆われている場合がある
        # つまり、座席(i,j)の状態は最大指示時間の方のorderに従う

        # これを考えて、行が最後に指示された時刻が tR[i], order oR[i]
        # 列が最後に指示された時刻が tC[j], order oC[j]

        # 状態 = if tR[i] > tC[j] then oR[i] else oC[j]

        # 自分は起立いくつか数えたい
        # r,c <= 50000のため全座席(25億)は無理

        # そこで、全列の指示時間tC,jとorder oC,j から順に集計しよう

        # 行側の指示時刻と注文をまとめておく

        # アイデア1: 行の指示時刻によってグループ化
        # アイデア2: 同様に列をグループ化
        # 起立の席数 = sum over all i,j of (状態==1)

        # これを計算するために、行のデータと列のデータをイベント順に操作する

        # 実装方針を変える：
        # 集計式を利用し、

        # 全座席のうち起立している座席数 = 起立行での列の状態と起立列での行の状態が上書きされているが計算が複雑

        # もっと簡単に次の計算を行う：
        # 起立している座席の数は
        # (起立行 * 起立していない列の数) + (起立していない行 * 起立列) から
        # (起立している行と起立している列の重複部分)を引く

        # つまり、
        # 起立行 = 行の指示で最後にorder=1で最大指示時間が最大の行
        # 起立列 = 列の指示で最後にorder=1で最大指示時間が最大の列

        # しかし一部座席で最後に指示された方が列か行かで状態が変わるので単純にこの計算はできない

        # そこで、次の簡単な方式を試す:

        # 1) 最後に指示されたのが行である座席は行のorder
        # 2) 最後に指示されたのが列である座席は列のorder

        # それぞれについて、行が最後に指示された時間で昇順に行をソートし
        # 同様に列で降順に並べて、
        # 行の指示の時間が列の指示の時間より小さいときは列の指示が勝つ、

        # 少し考えて以下の実装をする:

        # 行の指示時間とorderのセット作成
        # 列の指示時間とorderのセット作成

        # 同時に指示時間から数えられるよう昇順降順ソートする

        row_list = []
        for i in range(r):
            row_list.append((last_row_order[i],last_row_command[i]))
        col_list = []
        for j in range(c):
            col_list.append((last_col_order[j],last_col_command[j]))
        row_list.sort(reverse=True,key=lambda x:x[0]) # 指示時間大きい順
        col_list.sort(reverse=True,key=lambda x:x[0])
        # 各行が起立か判定(row起立行数)
        row_stand_count = 0
        row_order_map = {}
        for i,(t,o) in enumerate(row_list):
            row_order_map[t,o] = row_order_map.get((t,o),0)+1
            if o==1 and t!=-1:
                row_stand_count +=1
        # 同様列立っている列数
        col_stand_count = 0
        col_order_map = {}
        for j,(t,o) in enumerate(col_list):
            col_order_map[t,o] = col_order_map.get((t,o),0)+1
            if o==1 and t!=-1:
                col_stand_count +=1

        # ここまでのロジックは間違い
        # 元々の問題は、最終状態で立っている座席数を求めるだけなので、上のロジックを捨てて
        # 素直に 以下で行う:

        # 起立している座席数 = Σ i=0 to r-1 Σ j=0 to c-1 [状態(i,j) == 1]

        # 状態(i,j) = last_row_order[i], last_row_command[i], last_col_order[j], last_col_command[j]

        # 状態 = order of max(last_row_order[i], last_col_order[j])

        # 最大の方のorderを使う

        # これを効率的に数えるには、

        # 指示時刻の条件に基づいて計算

        # これを解く簡単なコードを以下に書く

        # 最大指示時刻の種類はq+1程度（-1～q-1）

        # last_row_orderに対応する行数の配列
        from collections import defaultdict
        row_time_count = defaultdict(int)
        for i in range(r):
            row_time_count[last_row_order[i]] +=1
        col_time_count = defaultdict(int)
        for j in range(c):
            col_time_count[last_col_order[j]] +=1

        # 次に、各座席について、「行の指示時間」と「列の指示時間」の大小比較により今の状態が決まる

        # row_order[i], row_command[i]で i=last_row_order の group がわかる

        # なので指示時間tごとに行数,列数がわかる

        # これを二重ループで計算:

        # Σ_(row_time, row_count) Σ_(col_time, col_count)
        # 乗算して各座席に対応
        # 状態はrow_time > col_time ? row_command : col_command

        # ただし -1は最初の指示なしでcommand=0

        # 各時間tで対応するcommandをdictから参照

        # まず、行のcommandはlast_row_commandから取得するためkeyの実体は分からないが、last_row_commandは座席ごとなので、ここは改めてまとめる。

        # なので行の時間 t に対応するcommandは、last_row_command にその時間のidxが存在した座標がある場合、そこからとる

        # しかし複数の行に同じ時間tがあるはずなのでcommandは同じである必要がある

        # なので最初にlast_row_order[i]とlast_row_command[i]のペアをdictで作成する

        row_command_dict = {}
        for i in range(r):
            t = last_row_order[i]
            o = last_row_command[i]
            if t not in row_command_dict:
                row_command_dict[t] = o
        col_command_dict = {}
        for j in range(c):
            t = last_col_order[j]
            o = last_col_command[j]
            if t not in col_command_dict:
                col_command_dict[t] = o
        # -1のときcommandは0でないといけない
        if -1 not in row_command_dict:
            row_command_dict[-1] = 0
        if -1 not in col_command_dict:
            col_command_dict[-1] = 0
        # 計算開始
        ans = 0
        # row_time_countとcol_time_countはdefaultdictなのでkeyの組み合わせすべて計算
        for rt, rcnt in row_time_count.items():
            for ct, ccnt in col_time_count.items():
                if rt > ct:
                    # 最終状態はrow_command_dict[rt]
                    if row_command_dict[rt] == 1:
                        ans += rcnt*ccnt
                else:
                    # ct >= rt
                    # 最終状態はcol_command_dict[ct]
                    if col_command_dict[ct] ==1:
                        ans += rcnt*ccnt
        print(ans)

main()