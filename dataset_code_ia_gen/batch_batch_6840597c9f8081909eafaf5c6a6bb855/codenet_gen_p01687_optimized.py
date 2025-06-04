from collections import Counter

def restore_string(D):
    target = "AIZUNYAN"
    anagram_chars = sorted("AIDUNYAN")
    n = len(D)
    res = []
    i = 0
    while i < n:
        if i + 8 <= n:
            window = D[i:i+8]
            if sorted(window) == anagram_chars:
                res.append(target)
                i += 8
                continue
        res.append(D[i])
        i += 1
    return "".join(res)

D = input()
print(restore_string(D))