from bisect import bisect_right

def find_all(char, string):
    return [i for i, c in enumerate(string) if c == char]

def signboard(s, t):
    if s in t:
        return True

    positions_first = find_all(s[0], t)
    positions_second = find_all(s[1], t)
    if not positions_first or not positions_second:
        return False

    len_t = len(t)
    len_s = len(s)

    for start in positions_first:
        idx = bisect_right(positions_second, start)
        for second_pos in positions_second[idx:]:
            step = second_pos - start
            if start + step * (len_s - 1) >= len_t:
                break
            if all(s[i] == t[start + i * step] for i in range(len_s)):
                return True
    return False

n = int(input())
a = input().strip()
strings = [input().strip() for _ in range(n)]

print(sum(signboard(a, b) for b in strings))