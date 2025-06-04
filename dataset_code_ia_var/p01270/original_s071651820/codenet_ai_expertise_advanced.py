from sys import stdin, exit
from bisect import insort

def main():
    input_iter = iter(stdin.readline, '')
    while True:
        try:
            N = int(next(input_iter))
        except StopIteration:
            break
        if N == 0:
            exit()
        data = []
        emp = [[0, 10**9]]
        for _ in range(N):
            tmp = next(input_iter).split()
            if tmp[0] == "W":
                c, k = int(tmp[1]), int(tmp[2])
                while k:
                    start, end = emp[0]
                    width = end - start
                    alloc = min(k, width)
                    data.append((c, [start, start + alloc]))
                    if alloc == width:
                        emp.pop(0)
                    else:
                        emp[0][0] += alloc
                    k -= alloc
            elif tmp[0] == "D":
                c = int(tmp[1])
                freed = [rng for cid, rng in data if cid == c]
                data = [i for i in data if i[0] != c]
                for rng in freed:
                    insort(emp, rng)
                # Merge contiguous or overlapping intervals
                merged = []
                for rng in emp:
                    if not merged or merged[-1][1] < rng[0]:
                        merged.append(rng)
                    else:
                        merged[-1][1] = max(merged[-1][1], rng[1])
                emp = merged
            else:  # "S"
                s = int(tmp[1])
                idx = next((cid for cid, rng in data if rng[0] <= s < rng[1]), -1)
                print(idx)
        print()

main()