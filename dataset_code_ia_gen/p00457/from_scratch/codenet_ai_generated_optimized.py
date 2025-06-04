import sys
sys.setrecursionlimit(10**7)

def chain_reaction(chars):
    # chars: list of colors
    n = len(chars)
    stack = []
    for c in chars:
        if not stack or stack[-1][0] != c:
            stack.append([c, 1])
        else:
            stack[-1][1] += 1
            if stack[-1][1] >= 4:
                stack.pop()
    # reconstruct after removals
    result = []
    for color, count in stack:
        result.extend([color]*count)
    # If chain reactions still possible:
    if len(result) == n:
        return result
    else:
        return chain_reaction(result)

def solve():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        chars = [int(input()) for _ in range(N)]
        min_remaining = N
        for i in range(N):
            original = chars[i]
            for c in (1,2,3):
                if c == original:
                    continue
                new_chars = chars[:]
                new_chars[i] = c
                final = chain_reaction(new_chars)
                if len(final) < min_remaining:
                    min_remaining = len(final)
        print(min_remaining)

if __name__ == "__main__":
    solve()