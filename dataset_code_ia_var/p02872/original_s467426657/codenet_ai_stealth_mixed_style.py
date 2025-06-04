import copy
import sys

def deleteProduct(nowPos):
    global product
    idx = len(product) - 1
    while idx >= 0:
        if nowPos == product[idx][2]:
            del product[idx]
        idx -= 1

def getDistance(src, dst):
    global route, temp_node

    temp_node.clear()
    temp_node = [[] for _ in range(V)]

    NODE_ROUTE, NODE_DEFINED, NODE_COST, NODE_CHG_FROM = 0, 1, 2, 3

    for v in range(V):
        temp_node[v].append(copy.deepcopy(es[v]))
        temp_node[v].append(0)
        temp_node[v].append(-1)
        temp_node[v].append(0)

    temp_node[dst][NODE_COST] = 0
    distance = 100

    while True:
        i = None
        for k in range(V):
            if temp_node[k][NODE_DEFINED] == 0 and temp_node[k][NODE_COST] >= 0:
                i = k
                break
        all_defined = True
        for x in temp_node:
            if x[NODE_DEFINED] == 0:
                all_defined = False
        if all_defined or i is None:
            break
        temp_node[i][NODE_DEFINED] = 1
        for edge in temp_node[i][NODE_ROUTE]:
            to = edge[0]
            cost = temp_node[i][NODE_COST] + edge[1]
            if temp_node[to][NODE_COST] < 0:
                temp_node[to][NODE_COST] = cost
                temp_node[to][NODE_CHG_FROM] = i
            elif temp_node[to][NODE_COST] > cost:
                temp_node[to][NODE_COST] = cost
                temp_node[to][NODE_CHG_FROM] = i

    rnum, distance, i, cost = 0, 0, src, 0
    route.clear()
    while True:
        cost += temp_node[i][NODE_COST]
        if dst == i:
            distance = cost
            break
        prev, i = i, temp_node[i][NODE_CHG_FROM]
        route.append([i, 0])
        for j in range(len(temp_node[prev][0])):
            if temp_node[prev][0][j][0] == route[rnum][0]:
                route[rnum][1] = temp_node[prev][0][j][1]
        distance += route[rnum][1]
        rnum += 1
    return distance

route = []
def getTargetPos(now_pos):
    global product, pos, route
    try:
        return product[0][2]
    except Exception:
        return -1

product=[]
def getProduct(currentTime):
    for i, o in enumerate(order):
        if time_step_before <= o[0] <= currentTime:
            product.append(copy.deepcopy(o))

def gotoVertex(x, y):
    global nowPos, route, total_move_count
    nowPos = -1
    print(route[0][0]+1, flush=True)
    route[0][1] -= 1
    if route[0][1] == 0:
        deleteProduct(route[0][0])
        nowPos = route[0][0]
        del route[0]

def initProduct(nowPos):
    global temp_node, product
    getDistance(nowPos, V-2)
    for i in range(len(product)):
        for j in range(len(temp_node)):
            if product[i][2] == j:
                product[i][3] = temp_node[j][2]
                break
    product = sorted(product, key=lambda z: z[3])

V, E = map(int, input().split())
es = [[] for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    es[a].append([b, c])
    es[b].append([a, c])

F = list(map(int, input().split()))
T = int(input())
order = []
temp_node = [[] for _ in range(V)]
total_move_count = 0
nowPos = 0
targetPos = -1
time_step = 0
time_step_before = 0

for i in range(T):
    Nnew = int(input())
    for _ in range(Nnew):
        new_id, dst = map(int, input().split())
        order.append([time_step, new_id, (dst-1), 0])
    Nput = int(input())
    for _ in range(Nput):
        put_id = int(input())
    if total_move_count >= T:
        break
    if nowPos == 0:
        getProduct(time_step)
        time_step_before = time_step
        if len(product) != 0:
            time_step = time_step
        else:
            print(-1, flush=True)
            time_step = time_step + 1
            total_move_count += 1
            if total_move_count >= T:
                break
    if len(product) != 0:
        targetPos = getTargetPos(nowPos)
        if len(route) == 0:
            getDistance(nowPos, targetPos)
        gotoVertex(nowPos, targetPos)
        time_step += 1
    if len(product) == 0 and nowPos != 0:
        if len(route) == 0:
            getDistance(nowPos, 0)
        gotoVertex(nowPos, 0)
        time_step += 1
    vardict = input()
    if vardict == 'NG':
        sys.exit()
    Nachive = int(input())
    for _ in range(Nachive):
        achive_id = int(input())