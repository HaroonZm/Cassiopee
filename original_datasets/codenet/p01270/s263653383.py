from bisect import bisect_right
while True:
    N = int(input())
    if N==0:
        break
    mem = []  # (l, r, id)
    for _ in range(N):
        command = input().split()
        if command[0]=="W":
            Id, S = map(int, command[1:])
            subS = S
            idx_mem = 0
            idx = 0
            while idx_mem < len(mem):
                l, r, _ = mem[idx_mem]
                if idx != l:
                    space = l - idx
                    assert space > 0, (mem, l, idx)
                    if subS <= space:
                        mem.insert(idx_mem, [idx, idx+subS, Id])
                        subS = 0
                        break
                    else:
                        mem.insert(idx_mem, [idx, idx+space, Id])
                        subS -= space
                        idx_mem += 1
                idx = r
                idx_mem += 1
            else:
                mem.append([idx, idx+subS, Id])

        elif command[0]=="D":
            Id = int(command[1])
            for idx_mem in range(len(mem)-1, -1, -1):
                if mem[idx_mem][2] == Id:
                    del mem[idx_mem]
        else:
            P = int(command[1])
            idx_mem = bisect_right(mem, [P, 100000000000000, -1]) - 1
            #print(mem, idx_mem)
            if idx_mem==-1:
                print(-1)
            else:
                l, r, id_ = mem[idx_mem]
                if P < r:
                    print(id_)
                else:
                    print(-1)
    print()