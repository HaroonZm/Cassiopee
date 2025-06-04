def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or n < m:
        return []
    # Preprocess pattern to build longest prefix suffix (lps) array
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    # Search phase
    res = []
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                res.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res

T = input()
P = input()
indices = kmp_search(T, P)
for idx in indices:
    print(idx)