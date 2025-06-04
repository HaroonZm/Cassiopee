def solve():
    N = int(input())
    T0 = []
    T1 = []
    total = 0

    for i in range(N):
        s = input()
        open_needed = 0
        for c in s:
            if c == '(':
                open_needed += 1
            elif open_needed > 0:
                open_needed -= 1
        close_needed = 0
        for c in reversed(s):
            if c == ')':
                close_needed += 1
            elif close_needed > 0:
                close_needed -= 1
        if close_needed < open_needed:
            T0.append((close_needed, open_needed))
        else:
            T1.append((open_needed, close_needed))
        total += open_needed - close_needed

    if total != 0:
        print("No")
        return

    def check(lst):
        used = [False] * len(lst)
        curr = 0
        for x in range(len(lst)):
            selected = -1
            best = (-1000, -1000)
            for y in range(len(lst)):
                if not used[y]:
                    b, a = lst[y]
                    if b <= curr:
                        if (a - b, b) > best:
                            best = (a - b, b)
                            selected = y
            if selected == -1:
                return False
            used[selected] = True
            b, a = lst[selected]
            curr += (a - b)
        return True

    if check(T0) and check(T1):
        print("Yes")
    else:
        print("No")

solve()