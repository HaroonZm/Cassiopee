import sys

SEATS = 17
GROUPS = 100

# 事前計算
groups = []
for i in range(GROUPS):
    arrival = 5 * i
    size = 5 if i % 5 == 1 else 2
    eat = 17 * (i % 2) + 3 * (i % 3) + 19
    groups.append({'arrival': arrival, 'size': size, 'eat': eat})

def can_seat(seats, size):
    count = 0
    start = -1
    for i, s in enumerate(seats):
        if s == -1:
            count += 1
            if count == size:
                return i - size + 1
        else:
            count = 0
    return -1

for line in sys.stdin:
    n = line.strip()
    if not n.isdigit():
        continue
    n = int(n)
    # 初期化
    seats = [-1] * SEATS
    queue = []
    wait_start = [-1]*GROUPS
    seated_time = [-1]*GROUPS
    leave_time = [-1]*GROUPS
    seated = [False]*GROUPS

    time = 0
    arrived_set = set()
    def all_arrived(t):
        return t > groups[-1]['arrival']

    # グループ到着時刻で止めずタイムライン
    max_time = 10**6
    while True:
        # 退出処理
        for i in range(GROUPS):
            if leave_time[i] == time:
                # 席解放
                for idx in range(SEATS):
                    if seats[idx] == i:
                        seats[idx] = -1
        # 到着グループ追加
        for i in range(GROUPS):
            if groups[i]['arrival'] == time:
                if len(queue) > 0 or can_seat(seats, groups[i]['size']) == -1:
                    queue.append(i)
                    wait_start[i] = time
                else:
                    pos = can_seat(seats, groups[i]['size'])
                    for idx in range(pos, pos + groups[i]['size']):
                        seats[idx] = i
                    seated_time[i] = time
                    leave_time[i] = time + groups[i]['eat']
                    seated[i] = True

        # 行列から着席可能なグループを順に案内
        while queue:
            front = queue[0]
            pos = can_seat(seats, groups[front]['size'])
            if pos == -1:
                break
            # 着席
            for idx in range(pos, pos + groups[front]['size']):
                seats[idx] = front
            seated_time[front] = time
            leave_time[front] = time + groups[front]['eat']
            seated[front] = True
            queue.pop(0)

        # 待ち時間計算で早期終了可能
        if seated[n]:
            break
        time += 1
        if time > max_time:
            break

    wait = seated_time[n] - groups[n]['arrival'] if seated_time[n]>=0 else 0
    print(wait)