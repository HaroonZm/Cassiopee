from collections import defaultdict
d = defaultdict(int)

def main(s, x=1):
    f = True
    l = 0
    r = 0
    index = float("INF")
    res = 0
    i = 0
    lis = []
    if x:
        while i < len(s):
            if s[i].isupper():
                tmp = s[i]
                i += 1
                while i < len(s) and s[i].islower():
                    tmp += s[i]
                    i += 1
                lis.append(tmp)

            elif s[i].isdecimal():
                tmp = s[i]
                i += 1
                while i < len(s) and s[i].isdecimal():
                    tmp += s[i]
                    i += 1
                lis.append(tmp)

            else:
                lis.append(s[i])
                i += 1
    else:
        lis = s
    s = lis
    ans = 0
    i = 0
    # print(s,x)
    while i < len(s):
        if s[i] == "(":
            f = False
            l += 1
            index = min(index, i)

        elif s[i] == ")":
            r += 1
            if l == r:
                res = main(s[index + 1 :i], 0)
                if res == "UNKNOWN":
                    return res
                f = True
                if i != len(s) - 1:
                    if s[i + 1].isdecimal():
                        i += 1
                        res *= int(s[i])
                ans += res
                index = float("INF")
                l = 0
                r = 0
        
        else:
            if f:
                if not (s[i] in d.keys()):
                    return "UNKNOWN"
                res = d[s[i]]
                if i != len(s) - 1:
                    if s[i + 1].isdecimal():
                        i += 1
                        res *= int(s[i])
                ans += res

        i += 1
    return ans

if __name__ == "__main__":
    while 1:
        n = input()
        if n == "END_OF_FIRST_PART":
            break
        a, b = n.split()
        b = int(b)
        d[a] = b
    while 1:
        n = input()
        if n == "0":
            break
        print(main(n))