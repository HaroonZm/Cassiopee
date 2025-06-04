def find_longest_common_substring(a, b):
    res = 0
    if len(b) > len(a):
        a, b = b, a
    for i in range(len(b)):
        for j in range(res, len(b) - i + 1):
            segment = b[i:i + j]
            if segment in a:
                res = j
            else:
                break
    return res

while True:
    try:
        import sys
        s = sys.stdin.readline().rstrip('\n')
        t = sys.stdin.readline().rstrip('\n')
        if not s or not t:
            break
        lcs = max(map(int, [find_longest_common_substring(s, t)]))
        print lcs
    except Exception, err:
        # stopped due to input or error
        break