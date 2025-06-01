from collections import deque

def fix(alst, blst, floar, buil, n):
    lst = alst if buil == 0 else blst
    if lst[floar] == 0:
        return floar
    elif lst[floar] == 1:
        while floar + 1 < n and lst[floar + 1] == 1:
            floar += 1
        return floar
    else:
        while floar >= 0 and lst[floar] == 2:
            floar -= 1
        return floar

def search(alst, blst, n):
    from collections import deque as dq
    que = dq()
    init_floar_a = fix(alst, blst, 0, 0, n)
    init_floar_b = fix(alst, blst, 0, 1, n)
    if n-1 in (init_floar_a, init_floar_b):
        print(0)
        return
    que.append([0, init_floar_a, 0])
    que.append([0, init_floar_b, 1])
    visited = dict()
    visited[(0, init_floar_a)] = 0
    visited[(0, init_floar_b)] = 0

    while len(que) > 0:
        total, floor, buil = que.popleft()
        next_buil = 1 - buil
        for step in range(3):
            new_pos = floor + step
            if new_pos >= n:
                break
            target = fix(alst, blst, new_pos, next_buil, n)
            if target == n -1:
                print(total + 1)
                return
            key = (target, next_buil)
            if key not in visited:
                visited[key] = total + 1
                que.append((total + 1, target, next_buil))
    print("NA")

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a_line = input().strip()
        b_line = input().strip()
        alst = list(map(int, a_line.split()))
        blst = list(map(int, b_line.split()))
        search(alst, blst, n)

main()