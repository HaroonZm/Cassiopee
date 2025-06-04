import copy
V, E = map(int, input().split())
es = [[] for i in range(V)]
for i in range(E):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    es[a].append([b, c])
    es[b].append([a, c])
F = list(map(int, input().split()))
T = int(input())
order = []
product = []
temp_node = [[] for _ in range(V)]
route = []
nowPos = 0
targetPos = -1
total_move_count = 0
time_step = 0
time_step_before = 0
import sys

for i in range(T):
    Nnew = int(input())
    for j in range(Nnew):
        new_id, dst = map(int, input().split())
        order.append([time_step, new_id, (dst-1), 0])
    Nput = int(input())
    for j in range(Nput):
        put_id = int(input())
    if total_move_count >= T:
        break
    if nowPos == 0:
        for ii in range(len(order)):
            if time_step_before <= order[ii][0] <= time_step:
                product.append(copy.deepcopy(order[ii]))
        time_step_before = time_step
    if nowPos == 0:
        if len(product) != 0:
            pass
        else:
            print(-1, flush=True)
            time_step = time_step + 1
            total_move_count = total_move_count + 1
            if total_move_count >= T:
                break
    if len(product) != 0:
        pos = (product[0][2])
        targetPos = pos
        if len(route) == 0:
            temp_node.clear()
            temp_node = [[] for _ in range(V)]
            NODE_ROUTE = 0
            NODE_DEFINED = 1
            NODE_COST = 2
            NODE_CHG_FROM = 3
            for iii in range(V):
                temp_node[iii].append(copy.deepcopy(es[iii]))
                temp_node[iii].append(0)
                temp_node[iii].append(-1)
                temp_node[iii].append(0)
            temp_node[targetPos][NODE_COST] = 0
            while True:
                for kk in range(V):
                    if temp_node[kk][NODE_DEFINED] == 1 or temp_node[kk][NODE_COST] < 0:
                        continue
                    else:
                        break
                loop_end_flag = 1
                for mm in range(len(temp_node)):
                    if temp_node[mm][NODE_DEFINED] == 0:
                        loop_end_flag = 0
                if loop_end_flag == 1:
                    break
                temp_node[kk][NODE_DEFINED] = 1
                for jjj in range(len(temp_node[kk][NODE_ROUTE])):
                    temp_node_to = temp_node[kk][NODE_ROUTE][jjj][0]
                    temp_node_cost = temp_node[kk][NODE_COST] + temp_node[kk][NODE_ROUTE][jjj][1]
                    if temp_node[temp_node_to][NODE_COST] < 0:
                        temp_node[temp_node_to][NODE_COST] = temp_node_cost
                        temp_node[temp_node_to][NODE_CHG_FROM] = kk
                    elif temp_node[temp_node_to][NODE_COST] > temp_node_cost:
                        temp_node[temp_node_to][NODE_COST] = temp_node_cost
                        temp_node[temp_node_to][NODE_CHG_FROM] = kk
            cost = 0
            route_num = 0
            ii = nowPos
            route.clear()
            distance = 0
            while True:
                cost = cost + temp_node[ii][NODE_COST]
                if targetPos == ii:
                    break
                moto_node = ii
                ii = temp_node[ii][NODE_CHG_FROM]
                route.append([ii, 0])
                for jj in range(len(temp_node[moto_node][0])):
                    if temp_node[moto_node][0][jj][0] == route[route_num][0]:
                        route[route_num][1] = temp_node[moto_node][0][jj][1]
                distance = distance + route[route_num][1]
                route_num += 1
        nowPos_local = -1
        print(route[0][0]+1, flush=True)
        route[0][1] = route[0][1] - 1
        if route[0][1] == 0:
            # deleteProduct
            for d_i in reversed(range(len(product))):
                if route[0][0] == product[d_i][2]:
                    del product[d_i]
            nowPos = route[0][0]
            del route[0]
        time_step = time_step + 1
    if len(product) == 0 and nowPos != 0:
        if len(route) == 0:
            temp_node.clear()
            temp_node = [[] for _ in range(V)]
            NODE_ROUTE = 0
            NODE_DEFINED = 1
            NODE_COST = 2
            NODE_CHG_FROM = 3
            for iii in range(V):
                temp_node[iii].append(copy.deepcopy(es[iii]))
                temp_node[iii].append(0)
                temp_node[iii].append(-1)
                temp_node[iii].append(0)
            temp_node[0][NODE_COST] = 0
            while True:
                for kk in range(V):
                    if temp_node[kk][NODE_DEFINED] == 1 or temp_node[kk][NODE_COST] < 0:
                        continue
                    else:
                        break
                loop_end_flag = 1
                for mm in range(len(temp_node)):
                    if temp_node[mm][NODE_DEFINED] == 0:
                        loop_end_flag = 0
                if loop_end_flag == 1:
                    break
                temp_node[kk][NODE_DEFINED] = 1
                for jjj in range(len(temp_node[kk][NODE_ROUTE])):
                    temp_node_to = temp_node[kk][NODE_ROUTE][jjj][0]
                    temp_node_cost = temp_node[kk][NODE_COST] + temp_node[kk][NODE_ROUTE][jjj][1]
                    if temp_node[temp_node_to][NODE_COST] < 0:
                        temp_node[temp_node_to][NODE_COST] = temp_node_cost
                        temp_node[temp_node_to][NODE_CHG_FROM] = kk
                    elif temp_node[temp_node_to][NODE_COST] > temp_node_cost:
                        temp_node[temp_node_to][NODE_COST] = temp_node_cost
                        temp_node[temp_node_to][NODE_CHG_FROM] = kk
            cost = 0
            route_num = 0
            ii = nowPos
            route.clear()
            distance = 0
            while True:
                cost = cost + temp_node[ii][NODE_COST]
                if 0 == ii:
                    break
                moto_node = ii
                ii = temp_node[ii][NODE_CHG_FROM]
                route.append([ii, 0])
                for jj in range(len(temp_node[moto_node][0])):
                    if temp_node[moto_node][0][jj][0] == route[route_num][0]:
                        route[route_num][1] = temp_node[moto_node][0][jj][1]
                distance = distance + route[route_num][1]
                route_num += 1
        nowPos_local = -1
        print(route[0][0]+1, flush=True)
        route[0][1] = route[0][1] - 1
        if route[0][1] == 0:
            # deleteProduct at shop
            for d_i in reversed(range(len(product))):
                if route[0][0] == product[d_i][2]:
                    del product[d_i]
            nowPos = route[0][0]
            del route[0]
        time_step = time_step + 1
    vardict = input()
    if vardict == 'NG':
        sys.exit()
    Nachive = int(input())
    for j in range(Nachive):
        achive_id = int(input())