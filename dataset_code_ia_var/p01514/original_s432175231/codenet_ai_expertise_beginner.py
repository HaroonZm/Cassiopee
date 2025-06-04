import sys

def main():
    while True:
        tpr = raw_input()
        t_str = tpr.strip().split()
        t = int(t_str[0])
        p = int(t_str[1])
        r = int(t_str[2])
        if t == 0 and p == 0 and r == 0:
            break
        record = []
        for i in range(t):
            # each team: solved_list, wrong_list, time, team_id
            record.append([[], [], 0, i+1])
        for i in range(r):
            line = raw_input()
            split_line = line.strip().split()
            tid = int(split_line[0])
            pid = int(split_line[1])
            time = int(split_line[2])
            message = split_line[3]
            team = record[tid-1]
            if message == 'CORRECT':
                if pid not in team[0]:
                    team[0].append(pid)
                    team[2] += team[1].count(pid) * 1200 + time
            elif message == 'WRONG':
                team[1].append(pid)
        sorted_rec = sorted(record, key=lambda x: (-len(x[0]), x[2]))
        for e in sorted_rec:
            print e[3], len(e[0]), e[2]

if __name__ == '__main__':
    main()