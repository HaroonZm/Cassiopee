def solve():
    import sys
    sys.setrecursionlimit(10**7)

    def backtrack(idx, cwords, candidates, c2p, p2c, used_candidate):
        if idx == len(cwords):
            return [list(p2c[word]) for word in used_candidate]

        cword = cwords[idx]
        res = []
        used = []
        for w in candidates[len(cword)]:
            # check mapping consistency between cword and w
            tmp_c2p = c2p.copy()
            tmp_p2c = p2c.copy()
            ok = True
            for cc, pc in zip(cword, w):
                if cc in tmp_c2p and tmp_c2p[cc] != pc:
                    ok = False
                    break
                if pc in tmp_p2c and tmp_p2c[pc] != cc:
                    ok = False
                    break
                tmp_c2p[cc] = pc
                tmp_p2c[pc] = cc
            if ok:
                used_candidate.append(w)
                result = backtrack(idx + 1, cwords, candidates, tmp_c2p, tmp_p2c, used_candidate)
                if result is not None:
                    if res and result != res:
                        return None  # multiple distinct results
                    res = result
                used_candidate.pop()
        if not res:
            return None
        return res

    input_lines = sys.stdin.read().split('\n')
    pos = 0
    while True:
        if pos>=len(input_lines): break
        n = input_lines[pos].strip()
        pos += 1
        if n == '0': break
        n = int(n)
        candidate_words = [input_lines[pos+i].strip() for i in range(n)]
        pos += n

        line = input_lines[pos].strip()
        pos += 1
        if not line.endswith('.'):
            print('-.')
            continue
        ciphertext_words = line[:-1].split()

        candidates = {}
        for w in candidate_words:
            candidates.setdefault(len(w), []).append(w)

        # backtrack to find plaintext words list
        # we want unique solution or else print -.
        # Because words length to candidate is limited, pruning is enough
        result = backtrack(0, ciphertext_words, candidates, {}, {}, [])
        if result is None:
            print('-.')
        else:
            print(' '.join(result)+'.')

if __name__ == "__main__":
    solve()