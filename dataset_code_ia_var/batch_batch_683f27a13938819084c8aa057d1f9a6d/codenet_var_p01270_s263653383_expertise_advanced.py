from bisect import bisect_right

def process_commands():
    import sys
    from collections import defaultdict

    input_iter = iter(sys.stdin.readline, "")
    while True:
        try:
            N_line = next(input_iter)
        except StopIteration:
            break
        N = int(N_line)
        if N == 0:
            break

        mem = []
        id_map = defaultdict(list) # id: list of (index in mem, start, end)

        for _ in range(N):
            command = next(input_iter).split()
            cmd_type = command[0]

            if cmd_type == "W":
                Id, S = map(int, command[1:])
                subS, idx, idx_mem = S, 0, 0
                while idx_mem < len(mem):
                    l, r, _id = mem[idx_mem]
                    if idx != l:
                        space = l - idx
                        if subS <= space:
                            item = [idx, idx + subS, Id]
                            mem.insert(idx_mem, item)
                            id_map[Id].append((idx_mem, idx, idx + subS))
                            subS = 0
                            break
                        else:
                            item = [idx, idx + space, Id]
                            mem.insert(idx_mem, item)
                            id_map[Id].append((idx_mem, idx, idx + space))
                            subS -= space
                            idx_mem += 1
                            idx = l
                            continue
                    idx = r
                    idx_mem += 1
                if subS > 0:
                    item = [idx, idx + subS, Id]
                    mem.append(item)
                    id_map[Id].append((len(mem)-1, idx, idx + subS))

                # Sync id_map indices after insertion
                for ID in id_map:
                    id_map[ID] = [(i if i >= idx_mem else i, s, e)
                                  for i, s, e in id_map[ID]]

            elif cmd_type == "D":
                Id = int(command[1])
                # batch delete using id_map
                indices = [i for i, _, _ in id_map.get(Id, ())]
                for i in reversed(sorted(indices)):
                    del mem[i]
                id_map.pop(Id, None)
                # fix id_map indices after deletions
                if indices:
                    shift = [0] * len(mem)
                    dec = 0
                    del_set = set(indices)
                    for i in range(len(mem) + len(indices)):
                        if i in del_set:
                            dec += 1
                        elif i - dec < len(mem):
                            shift[i - dec] = dec
                    for ID in id_map:
                        id_map[ID] = [(i - shift[i], s, e) for i, s, e in id_map[ID] if i not in del_set]

            else:  # cmd_type == "R"
                P = int(command[1])
                # Binary search for interval
                left, right = 0, len(mem)
                while left < right:
                    mid = (left + right) // 2
                    l, r, _ = mem[mid]
                    if r <= P:
                        left = mid + 1
                    else:
                        right = mid
                idx_mem = left if left < len(mem) and mem[left][0] <= P < mem[left][1] else -1
                print(mem[idx_mem][2] if idx_mem != -1 else -1)
        print()

process_commands()