import sys
sys.setrecursionlimit(10**7)

note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_up(n):
    return note_list[(note_list.index(n)+1)%12]

def note_down(n):
    return note_list[(note_list.index(n)-1)%12]

# k段にいる時に、i段に行く時に鳴る音を求める
def get_sound(k, i, T):
    if i == len(T)+1: # n+1段目(地上)に行くとき
        return T[i-1] 
    elif i > k:
        if i == k+1:
            return T[i-1]
        else: # i == k+2
            return note_up(T[i-1])
    else: # i == k-1 (戻る)
        return note_down(T[i-1])

def solve(n, m, T, S):
    # 0段目(雲)からスタート、m曲の順番通りに音を出したらn+1段目(地上)に降りる
    # kは現在の段数(0~n+1)
    # idxは現在までに出した曲の長さ
    from collections import deque
    queue = deque()
    queue.append((0,0))
    visited = set()
    visited.add((0,0))
    while queue:
        k, idx = queue.popleft()
        if idx == m and k == n+1:
            return "Yes"
        # 動ける段の候補
        candidates = []
        if k > 0: candidates.append(k-1)
        if k < n+1: candidates.append(k+1)
        if k < n : candidates.append(k+2)
        for i in candidates:
            if i < 0 or i > n+1:
                continue
            if k == 0 and i == 0:
                continue
            if k == 0 and i == 0:
                continue
            sound = get_sound(k, i, T)
            if idx == m:
                # 曲は全部終わってるから次は降りれる段だけ(つまりn+1段目)
                if i == n+1:
                    if (i, idx) not in visited:
                        visited.add((i, idx))
                        queue.append((i, idx))
                continue
            # 次の音の候補が曲の次の音と合っていたら
            if idx < m and sound == S[idx]:
                if (i, idx+1) not in visited:
                    # 雲には戻れない
                    if not (i == 0 and k != 0):
                        visited.add((i, idx+1))
                        queue.append((i, idx+1))
    return "No"

input_lines = sys.stdin.read().splitlines()
t = int(input_lines[0])
pos = 1
for _ in range(t):
    n, m = map(int, input_lines[pos].split())
    pos += 1
    T = input_lines[pos].split()
    pos += 1
    S = input_lines[pos].split()
    pos += 1
    print(solve(n,m,T,S))