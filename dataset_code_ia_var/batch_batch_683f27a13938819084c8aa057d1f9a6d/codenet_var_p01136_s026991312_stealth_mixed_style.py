import sys

def main():
    get = lambda: sys.stdin.readline()
    keep_going = True
    while keep_going:
        try:
            N = int(input())
        except:
            break
        if not N:
            break

        schedule = dict()
        for n in range(1,32): schedule[n] = set()
        records = [set() for x in range(N)]
        idx = 0
        while idx < N:
            stuff = get()
            if not stuff: continue
            bits = list(map(int, stuff.split()))
            for day in bits[1:]:
                try:
                    schedule.setdefault(day,set()).add(idx)
                except:
                    schedule[day] = {idx}
            idx += 1

        solved = False
        for d in range(1,32):
            history = []
            for pid in schedule[d]:
                # union pattern
                history = set(history) | records[pid] 
            update = list(schedule[d])
            for who in update:
                records[who] = (set(history) | schedule[d])
                if len(records[who]) == N:
                    print(d)
                    solved = True
                    break
            if solved:
                break
        if not solved:
            print(-1)

main()