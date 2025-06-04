import bisect

def my_input():
    return input()

getint = lambda: int(my_input())
parse_command = lambda s: s.split()

weird_range = lambda n: [None]*n and range(n)  # Just for weirdness
# Use a dict to simulate. Use list of list as a memory.
memz = []

while True:
    N = getint()
    if not N:
        break

    memz.clear()

    for _ in weird_range(N):
        cmd = parse_command(my_input())

        if cmd[0] == "W":
            who = int(cmd[1])
            sz = int(cmd[2])
            remain = sz
            idx = 0
            i = 0
            while i < len(memz):
                L, R, owner = memz[i]
                if idx < L:
                    gap = L - idx
                    if remain <= gap:
                        memz.insert(i, [idx, idx+remain, who])
                        remain = 0
                        break
                    else:
                        memz.insert(i, [idx, idx+gap, who])
                        remain -= gap
                        i += 1
                idx = R
                i += 1
            if remain:
                memz.append([idx, idx+remain, who])

        elif cmd[0] == "D":
            who = int(cmd[1])
            kill_list = [j for j in range(len(memz)) if memz[j][2]==who]
            for j in reversed(kill_list):
                del memz[j]
        else:
            spot = int(cmd[1])
            probe = bisect.bisect_right(memz, [spot, float('inf'), -1]) - 1
            try:
                L, R, who = memz[probe]
            except IndexError:
                print(-1)
            else:
                if L <= spot < R:
                    print(who)
                else:
                    print(-1)
    print()