import sys
import heapq
from typing import List, Tuple, Set

class ModernMansion:
    def __init__(self, m: int, n: int, switches: List[Tuple[int, int]]):
        self.m = m  # 東西方向の部屋数
        self.n = n  # 南北方向の部屋数
        self.switch_rooms = set(self._encode(x, y) for x, y in switches)
        # 扉状態の切り替えはグローバルなので状態を0か1で管理する
        # 状態0: 横扉閉, 縦扉開 (初期状態)
        # 状態1: 横扉開, 縦扉閉

    def _encode(self, x: int, y: int) -> int:
        # 部屋の座標を一意のIDに変換（列優先）
        return (y - 1) * self.m + (x - 1)
    
    def _decode(self, id: int) -> Tuple[int, int]:
        y, x = divmod(id, self.m)
        return (x + 1, y + 1)

    def neighbors(self, pos: int, door_state: int) -> List[int]:
        # posはエンコード済の部屋ID
        # door_stateが0のとき、東西は閉じているので移動不可、南北は開いているので移動可
        # door_stateが1のとき、東西は開いている、南北は閉じている
        x, y = self._decode(pos)
        nbrs = []
        if door_state == 0:
            # 横扉閉鎖：横移動不可
            # 縦扉開放：縦に移動可能
            if y > 1:
                nbrs.append(self._encode(x, y - 1))
            if y < self.n:
                nbrs.append(self._encode(x, y + 1))
        else:
            # 横扉開放：横に移動可能
            # 縦扉閉鎖：縦移動不可
            if x > 1:
                nbrs.append(self._encode(x - 1, y))
            if x < self.m:
                nbrs.append(self._encode(x + 1, y))
        return nbrs

    def shortest_time(self) -> int:
        start = self._encode(1, 1)
        goal = self._encode(self.m, self.n)

        # 状態空間は (pos, door_state)
        # door_state ∈ {0, 1}
        # スイッチのある部屋でスイッチを押すとdoor_stateが反転し+1分
        # 移動は1分
        # Dijkstraで最短時間求める

        INF = 10 ** 18
        dist = [[INF] * 2 for _ in range(self.m * self.n)]
        dist[start][0] = 0
        hq = [(0, start, 0)]  # (時間, 部屋ID, door_state)

        while hq:
            cost, pos, state = heapq.heappop(hq)
            if dist[pos][state] < cost:
                continue
            if pos == goal:
                return cost

            # 移動ルート
            for nxt in self.neighbors(pos, state):
                ncost = cost + 1
                if dist[nxt][state] > ncost:
                    dist[nxt][state] = ncost
                    heapq.heappush(hq, (ncost, nxt, state))

            # スイッチ押し(その部屋にスイッチがある場合のみ)
            if pos in self.switch_rooms:
                nstate = 1 - state
                ncost = cost + 1
                if dist[pos][nstate] > ncost:
                    dist[pos][nstate] = ncost
                    heapq.heappush(hq, (ncost, pos, nstate))
        return -1

class InputParser:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.k = 0
        self.switches: List[Tuple[int, int]] = []

    def parse(self):
        self.m, self.n, self.k = map(int, sys.stdin.readline().strip().split())
        for _ in range(self.k):
            x, y = map(int, sys.stdin.readline().strip().split())
            self.switches.append((x, y))

def main():
    parser = InputParser()
    parser.parse()
    mansion = ModernMansion(parser.m, parser.n, parser.switches)
    res = mansion.shortest_time()
    print(res)

if __name__ == "__main__":
    main()