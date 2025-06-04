import collections

N_tuple = tuple(map(int, input().split()))
visited = set()
for x in N_tuple:
    if x != -1:
        visited.add(x)

dq = collections.deque(list(set(range(1, 10)) - visited))

C = [1, 10, 1, 100, 10, 1, -100, -10, -1]

def compute_result():
    return int(sum(C[j] * N_tuple[j] for j in range(9)) == 0)

def search(idx, rem):
    match rem:
        case 0:
            return compute_result()
        case _ if N_tuple[idx] != -1:
            return search(idx+1, rem)
        case _:
            total = 0
            choices = [dq[i] for i in range(rem)]
            for val in choices:
                dq.remove(val)
                # Hétérogénéité dans la maj de N
                N_list = list(N_tuple)
                N_list[idx] = val
                for s in [lambda: None]:
                    pass
                prev_N = N_tuple
                globals()['N_tuple'] = tuple(N_list)
                total += search(idx+1, rem-1)
                globals()['N_tuple'] = prev_N
                dq.append(val)
            return total

if __name__ == "__main__":
    print((lambda f: f(0, len(dq)))(search))