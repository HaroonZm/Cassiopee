import sys
from collections import deque
from heapq import heapify, heappop, heappush

def decide_next_dst(cost, order):
    d = 0
    c = 0
    for key in order:
        if cost[key] > c:
            d = key
            c = cost[key]
    return (d, c)

def solve():
    inf = 10000000000
    input = sys.stdin.readline
    
    V, E = map(int, input().split())
    edge = dict()
    wf = dict()
    next_id = dict() #iからjに行くときにiの次に訪れる地点
    for i in range(V):
        edge[i] = dict()
        wf[i] = dict()
        next_id[i] = dict()
        for j in range(V):
            edge[i][j] = (0 if i == j else inf)
            next_id[i][j] = j
            wf[i][j] = (0 if i == j else inf)

    for _ in range(E):
        u, v, d = map(int, input().split())
        edge[u - 1][v - 1] = d
        edge[v - 1][u - 1] = d
        wf[u - 1][v - 1] = d
        wf[v - 1][u - 1] = d

    #全頂点最短経路と目的の頂点に向かうとき次に行くべき頂点の復元
    for k in range(V): 
        for i in range(V):
            for j in range(V):
                if wf[i][j] > wf[i][k] + wf[k][j]:
                    wf[i][j] = wf[i][k] + wf[k][j]
                    next_id[i][j] = next_id[i][k] 

    T = int(input())
    order = set()
    stuck_order = set()

    command = [None] * T
    heading = 0 #次に向かう地点
    dist_left = 0 #次に向かう地点までの残り距離
    final_dist = 0
    stuck_cost = [0 for _ in range(V)] 
    cost = [0 for _ in range(V)] 
    driver_hold = 0
    store_hold = 0

    for t in range(T):
        N = int(input()) #注文の発生
        if N == 1:
            new_id, dst = map(int, input().split())
            stuck_order |= {dst - 1}
            stuck_cost[dst - 1] += 1
            store_hold += 1

        if dist_left > 0: #移動中の場合そのまま移動を続ける
            command[t] = heading + 1
            dist_left -= 1
        
        else:
            if heading == 0: #店にいるときの処理
                if store_hold == driver_hold == 0: 
                    command[t] = -1
                    continue
                else:
                    order |= stuck_order
                    for key in order: 
                        cost[key] += stuck_cost[key]
                        stuck_cost[key] = 0
                    driver_hold = sum(cost)
                    stuck_order = set()
                    store_hold = 0
        
            if heading in order and heading > 0: #顧客のいる場所で荷物を積み下ろすとき
                order -= {heading} 
                driver_hold -= cost[heading]
                cost[heading] = 0

            current_id = heading #現在地の更新
            if len(order) > 0: #まだ配達すべき荷物があるとき
                if current_id == final_dist: #目的地に到着したときは残りの荷物で先に運ぶべき荷物を選ぶ
                    final_dist, max_hold = decide_next_dst(cost, order)
                    if driver_hold < store_hold and current_id > 0 and max_hold == 1: final_dist = 0  
            else: final_dist = 0 #荷物が無いので店に戻る
                
            heading = next_id[current_id][final_dist]
            dist_left = edge[current_id][heading] - 1
            command[t] = heading + 1

    for i in range(T): print(command[i])

    return 0

if __name__ == "__main__":
    solve()