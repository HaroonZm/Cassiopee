import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    teams = []
    for _ in range(n):
        data = input().split()
        id_ = int(data[0])
        times = list(map(int, data[1:]))
        total_sec = (times[0]*60 + times[1]) + (times[2]*60 + times[3]) + (times[4]*60 + times[5]) + (times[6]*60 + times[7])
        teams.append((total_sec, id_))
    teams.sort()
    # 優勝, 準優勝, ブービー賞（最下位より2番目は[-2]）
    print(teams[0][1])
    print(teams[1][1])
    print(teams[-2][1])