def match(pattern, addr):
    return all(p == '?' or p == a for p, a in zip(pattern, addr))

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    rules = []
    for _ in range(n):
        parts = input().split()
        rules.append((parts[0], parts[1], parts[2]))
    packets = [input() for _ in range(m)]
    legal = []
    for line in packets:
        src, dst, msg = line.split(' ', 2)
        verdict = 'deny'  # default
        # check rules in reverse priority
        for action, sp, dp in reversed(rules):
            if match(sp, src) and match(dp, dst):
                verdict = action
                break
        if verdict == 'permit':
            legal.append(line)
    print(len(legal))
    print('\n'.join(legal))