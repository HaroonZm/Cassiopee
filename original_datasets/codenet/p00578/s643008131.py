def solve():
    N = int(input())
    A = [0] + [int(i) for i in input().split()] + [0]
    A_edge = []
    # 頂点と底辺のみにデータを絞る
    up_flg = True
    for i in range(1, len(A) - 1):
        if up_flg:
            if A[i] > A[i + 1]:
                A_edge.append([A[i], up_flg])
                up_flg = not up_flg
        else:
            if A[i] < A[i + 1]:
                A_edge.append([A[i], up_flg])
                up_flg = not up_flg
    A_edge.sort()  # 沈んでいく順に並べ替え
    # 島を数える
    island_count = 1
    max_island_count = 1
    for i in range(len(A_edge) - 1):
        if A_edge[i][1]:
            island_count -= 1
        else:
            island_count += 1
        if A_edge[i][0] < A_edge[i + 1][0]:
            max_island_count = max(max_island_count, island_count)
    # 島の高さがすべて0の時の考慮
    if max(A) <= 0:
        max_island_count = 0
    print(max_island_count)

if __name__ == '__main__':
    solve()