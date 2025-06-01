from collections import deque
import sys

def get_top_floor(building, floor, n):
    # 階段なら一番上まで移動
    if building[floor] == 1:
        top = floor
        # 階段は2階以上にまたがるので上に重なっている間topを伸ばす
        while top + 1 < n and building[top + 1] == 1:
            top += 1
        return top
    # 滑る壁なら普通か階段の一番上まで滑る
    elif building[floor] == 2:
        pos = floor
        # 滑り始めの位置はfloorなのでposを伸ばす
        while pos + 1 < n and building[pos + 1] != 2:
            if building[pos + 1] == 0:
                pos += 1
            elif building[pos + 1] == 1:
                pos = get_top_floor(building, pos + 1, n)
                break
            else:
                break
        return pos
    else:
        # 普通の壁はそのまま
        return floor

def solve():
    input_data = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_data):
            break
        n_line = input_data[idx].strip()
        idx += 1
        if n_line == '0':
            break
        n = int(n_line)
        a_line = input_data[idx].strip().split()
        idx += 1
        b_line = input_data[idx].strip().split()
        idx += 1
        a = list(map(int, a_line))
        b = list(map(int, b_line))
        # 最下階は滑る壁にはならないので問題文の制約に従いチェックしなくて良い
        
        # 状態：(building, floor)
        # building:0 or 1
        # floor:0-indexedで階数を表す
        # ジャンプの回数を求める
        
        visited = [[False]*n for _ in range(2)]
        queue = deque()
        # 初期位置はどちらのビルの1階からも開始可能
        # 1階はindex0
        # はじめのはしご処理などはジャンプ後に行うのでfloorはそのまま
        # ここではジャンプ回数0でスタート
        queue.append((0,0,0)) # ビル0, 1階(0), ジャンプ0回
        queue.append((1,0,0)) # ビル1, 1階(0), ジャンプ0回
        visited[0][0] = True
        visited[1][0] = True
        ans = "NA"
        while queue:
            building, floor, dist = queue.popleft()
            # 最上階(n-1)に到達したら屋上に行ける
            if floor == n-1:
                ans = dist
                break
            # 次のジャンプは反対側のビルにジャンプ
            nxt_building = 1 - building
            # 同じ階、1つ上、2つ上のどれかにジャンプ可能
            for df in range(3):
                nxt_floor = floor + df
                if nxt_floor >= n:
                    continue
                # 次のビルの壁情報からジャンプした先の位置を決める
                if nxt_building == 0:
                    base_floor = nxt_floor
                    base_type = a[nxt_floor]
                else:
                    base_floor = nxt_floor
                    base_type = b[nxt_floor]
                # ジャンプ先の壁を踏んだ後の最終的な位置を決める
                if nxt_building == 0:
                    final_floor = get_top_floor(a, base_floor, n)
                else:
                    final_floor = get_top_floor(b, base_floor, n)
                # 訪問済みならスキップ
                if not visited[nxt_building][final_floor]:
                    visited[nxt_building][final_floor] = True
                    queue.append((nxt_building, final_floor, dist + 1))
        print(ans)

if __name__ == "__main__":
    solve()