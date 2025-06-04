def match_pattern(pattern, address):
    for p_char, a_char in zip(pattern, address):
        if p_char != '?' and p_char != a_char:
            return False
    return True

while True:
    line = input().strip()
    if not line:
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break

    rules = []
    for _ in range(n):
        parts = input().strip().split()
        # format: permit source-pattern dest-pattern OR deny source-pattern dest-pattern
        # store in order so index is priority (higher index is higher priority)
        action = parts[0]  # 'permit' or 'deny'
        source_pattern = parts[1]
        dest_pattern = parts[2]
        rules.append((action, source_pattern, dest_pattern))

    packets = []
    for _ in range(m):
        src, dst, msg = input().strip().split()
        packets.append((src, dst, msg))

    legal_packets = []

    for src, dst, msg in packets:
        decision = 'deny'  # default deny
        # check from last rule to first for priority
        for i in range(len(rules)-1, -1, -1):
            action, s_pat, d_pat = rules[i]
            if match_pattern(s_pat, src) and match_pattern(d_pat, dst):
                decision = action
                break
        if decision == 'permit':
            legal_packets.append((src, dst, msg))

    print(len(legal_packets))
    for p in legal_packets:
        print(*p)