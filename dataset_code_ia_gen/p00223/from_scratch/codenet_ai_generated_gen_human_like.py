from collections import deque

def solve():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        tx, ty = map(int, input().split())
        kx, ky = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(H)]

        # 移動方向 dx, dy (東、西,南,北)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 座標は1始まりなので、0始まりに変換する
        tx -= 1
        ty -= 1
        kx -= 1
        ky -= 1

        # BFSの状態: (たかゆきx, たかゆきy, かずゆきx, かずゆきy)
        visited = [[[[False]*W for _ in range(H)] for __ in range(W)] for ___ in range(H)]
        visited[ty][tx][ky][kx] = True
        queue = deque()
        queue.append((tx, ty, kx, ky, 0))

        ans = "NA"
        while queue:
            tx_, ty_, kx_, ky_, t = queue.popleft()
            if t >= 100:
                # 100以上はNA
                break

            if tx_ == kx_ and ty_ == ky_:
                ans = t
                break

            # 全方向の移動を試す
            for dx, dy in directions:
                ntx = tx_ + dx
                nty = ty_ + dy
                nkx = kx_ - dx
                nky = ky_ - dy

                # たかゆきの移動可能か判定
                if not (0 <= ntx < W and 0 <= nty < H) or grid[nty][ntx] == 1:
                    # 移動不可なら元の位置に戻る
                    ntx, nty = tx_, ty_

                # かずゆきの移動可能か判定
                if not (0 <= nkx < W and 0 <= nky < H) or grid[nky][nkx] == 1:
                    # 移動不可なら元の位置に戻る
                    nkx, nky = kx_, ky_

                # 移動後に同じ場所にいるかをチェック（すれ違いは不可）
                if ntx == nkx and nty == nky:
                    # 出会った
                    ans = t+1
                    queue.clear()
                    break

                if not visited[nty][ntx][nky][nkx]:
                    visited[nty][ntx][nky][nkx] = True
                    queue.append((ntx, nty, nkx, nky, t+1))
        print(ans)

if __name__ == "__main__":
    solve()