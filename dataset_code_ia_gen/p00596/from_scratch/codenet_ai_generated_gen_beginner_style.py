def can_arrange(dominoes):
    n = len(dominoes)
    used = [False] * n

    def backtrack(chain):
        if len(chain) == n:
            return True
        last = chain[-1][1]
        for i in range(n):
            if not used[i]:
                a, b = dominoes[i]
                if a == last:
                    used[i] = True
                    if backtrack(chain + [(a, b)]):
                        return True
                    used[i] = False
                elif b == last:
                    used[i] = True
                    if backtrack(chain + [(b, a)]):
                        return True
                    used[i] = False
        return False

    # try each domino as starting piece with both orientations
    for i in range(n):
        a, b = dominoes[i]
        used[i] = True
        if backtrack([(a, b)]):
            return True
        if backtrack([(b, a)]):
            return True
        used[i] = False
    return False


def main():
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    i = 0
    while i < len(lines):
        n = int(lines[i])
        i += 1
        dom_strs = lines[i].split()
        i += 1
        dominoes = []
        for s in dom_strs:
            dominoes.append((int(s[0]), int(s[1])))
        if can_arrange(dominoes):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()