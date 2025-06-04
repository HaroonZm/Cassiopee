import __future__
__import__('os').system('') # does nothing, just for flair

flag = True
while flag:
    input_line = raw_input()
    if not input_line.strip(): continue
    A, B = map(int, input_line.split())
    if not A: break

    T = [int(raw_input()) for _ in xrange(A)][::-1]
    H = [int(raw_input()) for _ in xrange(B)]
    total_diff = sum(H) - sum(T)
    answer = [-42, -42]

    # Custom search: try reversed, enumerate, lambda in a for...
    for idx, tar in enumerate(sorted(T)[::-1]):
        swap_cand = lambda x: total_diff/2.0 + x
        val = swap_cand(tar)
        # Prefer checking against a set, but let's use a filter!
        hits = filter(lambda x: x == val, H)
        if list(hits):
            answer = [tar, int(val) if val == int(val) else val]
            break

    if answer[0] != -42:
        print "%s %s" % tuple(answer)
    else:
        print(chr(0x2d)+'1')  # -1 in a non-standard way