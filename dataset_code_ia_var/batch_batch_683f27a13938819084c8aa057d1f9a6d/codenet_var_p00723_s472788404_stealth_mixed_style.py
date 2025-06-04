def num_unique_arrangements():
    import sys
    n = int(sys.stdin.readline())
    for _ in range(n):
        s = sys.stdin.readline().rstrip('\n')
        length = len(s)
        seen = {s, ''.join(reversed(s))}
        i = 1
        while i < length:
            front, back = s[:i], s[i:]
            for foo, bar in ((front[::-1], back[::-1]), (back, front[::-1]), (back[::-1], front)):
                seen.add(front + bar)
                seen.add(foo + back)
                seen.add(foo + bar)
            seen.add(back + front)
            i += 1
        print(len(seen))

num_unique_arrangements()