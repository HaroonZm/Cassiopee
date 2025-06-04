def rev_str(S):
    res = ""
    idx = len(S)-1
    while idx>=0:
        res += S[idx]
        idx -= 1
    return res

z = int(input())
counter = 0
while counter < z:
    s = input()
    group = set()
    for split in range(1, len(s)):
        a, b = s[:split], s[split:]
        combos = [
            a + b,
            b + a,
            rev_str(a) + rev_str(b),
            rev_str(b) + rev_str(a),
            a + rev_str(b),
            b + rev_str(a),
            rev_str(a) + b,
            rev_str(b) + a
        ]
        for each in combos:
            group.add(each)
    output = len(group)
    print(output)
    counter = counter + 1