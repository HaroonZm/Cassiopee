import sys
import bisect

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    paintings = [tuple(map(int, input().split())) for _ in range(N)]
    frames = [int(input()) for _ in range(M)]

    # 条件を満たすように絵の順序を決めるための重要なポイント:
    # 右隣との絵の価値と額縁の大きさが単調非減少である必要があります。
    # つまり、絵は (額縁サイズ, 価値) の順に非減少列になるように並べる必要があります。

    # アプローチ:
    # 1. 額縁は「サイズ」でソートし、利用可能なものを昇順に管理
    # 2. 絵はサイズ <= 額縁のサイズである必要があるので、
    #    絵をサイズの昇順、価値の昇順でソートする
    # 3. 抽出した絵を順に考え、現在の額縁から絵のサイズ以上の最小額縁サイズを探す。
    #    見つけたらその額縁を使用済みにして絵を展示可能とする。
    # 4. この過程で、価値も昇順で処理されているので条件は満たされる。

    # しかし、このままでは価値の単調非減少を保証できない。
    # そこで、"価値"の非減少制約を考慮すると、絵の価値の昇順に従って額縁を割り当てるということになる。

    # したがって、絵は (価値, サイズ) の順で昇順にソートし、額縁はサイズのみの昇順で管理する。

    # 額縁のサイズ一覧をソート
    frames.sort()
    # 絵は (価値, サイズ) の順でソート
    paintings_sorted = sorted(((v, s) for s, v in paintings))

    # フレームの利用管理を行うため、リストで保持し、
    # 各絵に対してサイズ>=sを満たす額縁を二分探索で探す。

    # framesは昇順であるため、二分探索で「絵のサイズ以上の最小額縁サイズ」を探し、
    # 見つかったインデックスの額縁を使い果たし削除する。

    used_count = 0
    from bisect import bisect_left

    # framesをリストとして、使用済みは削除していくとO(M^2)で遅いので、
    # 利用済み額縁を効率的に管理するため、pythonのbisectだけでは間に合わない。

    # 代替案として、collections.Counterで額縁のサイズごとの個数を管理し、
    # キーを昇順に保持して、各絵に対してキー >= sの最小キーを探す

    import collections
    frame_count = collections.Counter(frames)
    unique_frames = sorted(frame_count.keys())

    for v, s in paintings_sorted:
        # 二分探索でs以上の額縁サイズを探す
        idx = bisect.bisect_left(unique_frames, s)
        # idxがunique_framesの範囲内かチェック
        while idx < len(unique_frames):
            frame_size = unique_frames[idx]
            if frame_count[frame_size] > 0:
                # この額縁を使う
                frame_count[frame_size] -= 1
                if frame_count[frame_size] == 0:
                    # 0になったらunique_framesからは消さずに放置（無害）
                    pass
                used_count += 1
                break
            else:
                # 0なら次も探す
                idx += 1
        # idx == len(unique_frames)になると対応する額縁が無いのでスキップ

    print(used_count)

if __name__ == "__main__":
    main()