import sys
import bisect

def main():
    input = sys.stdin.readline

    while True:
        N = int(input())
        if N == 0:
            break

        # ファイルID => 拡張区間のリスト[(start, end), ...]
        file_intervals = dict()

        # 空き領域のリスト[(start, end), ...]（start, endはセクタ番号の区間、endはstartを含む終端）
        # 初期状態では何も書き込まれていないため、空き領域は無限に広がっていることとする
        # セクタ番号は最大10^9までアクセスが必要なので、これより大きい区間は切り捨て可能
        MAX_SECTOR = 10**9
        free_intervals = [(0, MAX_SECTOR)]

        # セクタ番号 => ファイルID を求めるために書き込んだ区間全体を管理
        # 書き込み済みの区間はファイルIDで管理（区間全体でファイルを特定）
        # file_id から各書き込み区間を管理し、その区間ごとに検索をする
        # 参照時は全書き込み区間を集合的に扱うため、全区間のstartでソートしたリストを準備
        # ⇒ 書き込み区間は file_written_intervals : [(start, end, file_id), ...]
        file_written_intervals = []

        # 空き領域の管理用関数
        # free_intervalsは、(start,end)の昇順ソートされたリスト、startでソート済み
        def allocate_sectors(need):
            """
            空き領域から「need」個のセクタを順に割り当てる
            途中で区間が足りなくなった場合は次の空き区間に移動して割り当て
            戻り値は割り当てた区間のリスト[(start,end), ...]
            空き領域を減らし、free_intervalsを更新する
            """
            result = []
            remain = need

            new_free_intervals = []
            idx = 0

            while remain > 0 and idx < len(free_intervals):
                f_start, f_end = free_intervals[idx]
                length = f_end - f_start + 1
                if length <= remain:
                    # 空き区間全体を割り当て
                    result.append((f_start, f_end))
                    remain -= length
                    # 空き区間は消滅するためnew_free_intervalsに追加しない
                else:
                    # 部分割り当て
                    result.append((f_start, f_start + remain -1))
                    # 空き区間を前半部分割り当てるので、未使用は後半部分
                    new_free_intervals.append((f_start + remain, f_end))
                    remain = 0
                idx += 1

            # 残りの空き区間を追加
            while idx < len(free_intervals):
                new_free_intervals.append(free_intervals[idx])
                idx +=1

            if remain > 0:
                # 割り当てられなかった（問題文では書き込みは常に空き領域に書き込むことが示唆されるが念のため）
                # この場合は途中まで割り当てて戻すため、空き領域を元に戻す
                # 実務上起きないと思われるが、ここはエラー回避のため残す
                pass

            # freeの更新
            free_intervals.clear()
            free_intervals.extend(new_free_intervals)

            return result

        # 空き領域を追加（削除時に呼ぶ）
        def add_free_interval(new_start, new_end):
            """
            new_startからnew_endまでの空き区間をfree_intervalsに追加し、
            隣接または重複する区間とマージする
            """
            # free_intervalsはstart昇順にソートされていることを利用
            # 新規区間を入れる位置を探索
            idx = bisect.bisect_left(free_intervals, (new_start, new_end))
            # 挿入位置の前後をマージする

            left = idx -1
            right = idx

            s = new_start
            e = new_end

            # 左隣とマージ可能ならマージ
            if left >= 0:
                ls, le = free_intervals[left]
                if le + 1 >= s:
                    s = ls
                    e = max(e, le)
                    del free_intervals[left]
                    idx -= 1

            # 右隣とマージ可能ならマージ
            while right < len(free_intervals):
                rs, re = free_intervals[right]
                if rs > e + 1:
                    break
                e = max(e, re)
                del free_intervals[right]

            # 新たな合成区間を挿入
            bisect.insort_left(free_intervals, (s,e))

        # 書き込み区間のindexをstartで管理（参照処理効率化用）
        # 書き込み区間は常に start でソートしておく
        # 書き込みコマンドのたびにファイルIDと区間を file_written_intervalsに追加し、最後に start でソート
        # 参照コマンド時に二分探索で該当区間を探す
        def refresh_sorted_intervals():
            file_written_intervals.sort(key=lambda x:x[0])

        # 参照関数
        def search_file_in_sector(p):
            """
            セクタpが含まれる書き込み区間を二分探索で探す
            見つかればファイルIDを返す、なければ -1
            """
            intervals = file_written_intervals
            # intervalsは(start, end, file_id)でstart昇順

            idx = bisect.bisect_right(intervals, (p, 10**15, 10**15)) - 1
            if idx < 0:
                return -1
            st, ed, fid = intervals[idx]
            if st <= p <= ed:
                return fid
            return -1

        for _ in range(N):
            line = input().rstrip('\n')
            if not line:
                continue
            parts = line.split()
            cmd = parts[0]
            if cmd == "W":
                # 書き込み
                I = int(parts[1])
                S = int(parts[2])
                # まずファイルのサイズS分を先頭空き領域から順に割り当て
                allocated = allocate_sectors(S)
                # ファイルID => 書き込み区間のリストを保持
                file_intervals[I] = allocated
                # 書き込み区間をfile_written_intervalsにも追加
                for (s,e) in allocated:
                    file_written_intervals.append((s,e,I))

            elif cmd == "D":
                # 削除
                I = int(parts[1])
                if I in file_intervals:
                    # ファイルの割り当て区間をfree_intervalsに戻す（マージ含む）
                    for (s,e) in file_intervals[I]:
                        add_free_interval(s,e)
                    # ファイルの区間情報削除
                    del file_intervals[I]
                    # file_written_intervalsは後でまとめてsortしなおす
                # 削除により重複する区間がなくなるので後でfile_written_intervalsを再構築

            elif cmd == "R":
                # 参照
                # 参照コマンド直前にfile_written_intervalsをstartでソート
                # ただし効率化のため変更があった時のみソートするほうが良いが今回は毎回ソートでOK
                # file_written_intervalsから現在のファイル割当が分かる
                # ただし現在のfile_written_intervalsには削除済み区間が残っているので、
                # これらはfile_intervalsに含まれるファイルだけの区間のみに絞る必要がある
                # なので、参照時はfile_written_intervalsを一度再構築する
                intervals = []
                for fid, ivs in file_intervals.items():
                    for (st, ed) in ivs:
                        intervals.append((st, ed, fid))
                file_written_intervals = intervals
                refresh_sorted_intervals()

                P = int(parts[1])
                # 検索
                fid = search_file_in_sector(P)
                print(fid)
        print()  # 各データセット後の空行

if __name__ == "__main__":
    main()