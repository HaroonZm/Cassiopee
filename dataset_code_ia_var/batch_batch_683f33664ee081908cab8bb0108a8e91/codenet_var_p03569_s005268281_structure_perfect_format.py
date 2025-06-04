def codefes17qc_c():
    s = str(input())

    # x除去して回文であることが成立条件
    nox = s.replace('x', '')
    noxrev = nox[::-1]
    if nox != noxrev:
        print(-1)
        return

    # 順sと逆sを見ていき、合わないところはxが入るところ
    srev = s[::-1]
    ins = 0
    i, j = 0, 0
    while i < len(s) and j < len(s):
        if s[i] == srev[j]:
            i += 1
            j += 1
        else:
            if s[i] != 'x' and srev[j] == 'x':
                ins += 1
                j += 1
            elif s[i] == 'x' and srev[j] != 'x':
                ins += 1
                i += 1

    ins += len(s) - min(i, j)
    ans = ins // 2
    print(ans)

codefes17qc_c()