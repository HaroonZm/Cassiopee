from collections import deque

# 3色のリストと、2つの色の組み合わせから変化後の色を返す辞書を定義する
colors = ['r', 'g', 'b']
# 2つの異なる色の組み合わせから、変化後の色を求める関数
def next_color(c1, c2):
    # c1とc2は異なる色である前提
    # 3色のうちc1とc2に含まれない色を返す
    for c in colors:
        if c != c1 and c != c2:
            return c

def all_same(s):
    # 全て同じ色かどうか判定
    return all(ch == s[0] for ch in s)

def solve(start):
    # BFSを用いる
    # 状態空間は文字列で表される虫の色の並び
    # 各秒ごとに1回だけ、隣接する異なる組の1ペアのみが同時に新しい色に変わる
    # 変化はどれが選ばれるか予測できないので、全ての場合を探索する
    queue = deque()
    seen = set()
    queue.append((start, 0))
    seen.add(start)

    while queue:
        state, time = queue.popleft()
        # すべて同じ色になったら終了
        if all_same(state):
            return time
        # 隣り合う色が異なるペアを全て探す
        n = len(state)
        for i in range(n-1):
            if state[i] != state[i+1]:
                # このペアだけが変わる
                nc = next_color(state[i], state[i+1])
                # 新しい状態を作る
                new_state = list(state)
                new_state[i] = nc
                new_state[i+1] = nc
                new_state_str = ''.join(new_state)
                if new_state_str not in seen:
                    seen.add(new_state_str)
                    queue.append((new_state_str, time+1))
    # すべて同じ色になることがない場合
    return "NA"

while True:
    line = input().strip()
    if line == '0':
        break
    result = solve(line)
    print(result)