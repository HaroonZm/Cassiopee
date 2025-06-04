def extract_chars(name):
    vowels = 'aiueo'
    chars = [name[0]]
    for i in range(len(name) - 1):
        if name[i] in vowels:
            chars.append(name[i+1])
    return ''.join(chars)

while True:
    n = int(input())
    if n == 0:
        break
    names = []
    for _ in range(n):
        names.append(input())
    codes_list = []
    for name in names:
        codes_list.append(extract_chars(name))
    max_len = max(len(c) for c in codes_list)
    ans = -1
    for k in range(1, max_len+1):
        used = set()
        ok = True
        for code in codes_list:
            prefix = code[:k] if len(code) >= k else code
            if prefix in used:
                ok = False
                break
            used.add(prefix)
        if ok:
            ans = k
            break
    print(ans)