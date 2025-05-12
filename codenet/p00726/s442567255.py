def main():
    def pearser(s, n):
        if s == "":
            return ""
        i = 0
        while 1:
            if not s[i].isdigit():break
            i += 1
        if i == 0:
            r = pearser(s[i + 1:], n - 1)
            return s[0] + r
        if s[i] == "(":
            r = Parentp(s[i:], n, int(s[:i]))
        else:
            r = s[i] * int(s[:i])
            if len(r) >= n:
                return r[:n]
            r += pearser(s[i+1:], n - len(r))
        return r

    def Parentp(s, n, p):
        if s == "": return ""
        b = 0
        c = 0
        i = 0
        while 1:
            if s[i] == "(":
                c += 1
            if s[i] == ")":
                c -= 1
            if c == 0:
                break
            i += 1
        r = pearser(s[b + 1:i], n)
        l = len(r)
        if l * p >= n:
            r = r * (n // l + 1)
            return r[:n]
        r = r * p
        r += pearser(s[i+1:], n - len(r))
        return r

    def m(s,n):
        n = int(n)
        r = pearser(s, n + 1)
        if len(r) <= n:
            print(0)
            return
        print(r[n])

    while 1:
        s, n = map(str, input().split())
        if s == n == "0":
            break
        m(s, n)

main()