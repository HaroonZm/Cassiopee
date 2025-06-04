from collections.abc import Iterator

def c_to_int(char: str) -> int:
    return ord(char) - ord('A')

def solve(s: str) -> list:
    count = 0
    table = []
    append = table.append
    for c in s:
        match c:
            case '+':
                count += 1
            case '-':
                count -= 1
            case '[' | ']' | '?':
                append(c)
                if c == '?':
                    count = 0
            case _:
                append((c_to_int(c) + count) % 26)
                count = 0
    table = [0 if x == '?' else x for x in table]
    return table

def rev(table: list) -> str:
    def gen(it: Iterator) -> str:
        res = []
        for x in it:
            if x == '[':
                segment = []
                depth = 1
                for y in it:
                    if y == '[':
                        depth += 1
                    elif y == ']':
                        depth -= 1
                    if depth == 0:
                        break
                    segment.append(y)
                res.append(gen(iter(segment))[::-1])
            elif x == ']':
                continue
            else:
                res.append(chr(x + 65))
        return ''.join(res)
    return gen(iter(table))

if __name__ == '__main__':
    import sys
    for S in sys.stdin:
        S = S.rstrip('\n')
        if S and S[0] == '.':
            break
        print(rev(solve(S)))