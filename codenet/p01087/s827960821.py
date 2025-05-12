def dfs(l):
    x = len(l[0])
    if l[0][-1] == "+":
        b = 0
        i = 1
        while i < len(l):
            if len(l[i]) == x + 1 and "0" <= l[i][-1] <= "9":
                b += int(l[i][-1])
                i += 1
            elif len(l[i]) == x + 1 and (l[i][-1] == "+" or l[i][-1] == "*"):
                f = i
                i += 1
                while i < len(l):
                    if len(l[i]) == x + 1:
                        break
                    i += 1
                b += dfs(l[f:i])

    elif l[0][-1] == "*":
        b = 1
        i = 1
        while i < len(l):
            if len(l[i]) == x + 1 and "0" <= l[i][-1] <= "9":
                b *= int(l[i][-1])
                i += 1
            elif len(l[i]) == x + 1 and (l[i][-1] == "+" or l[i][-1] == "*"):
                f = i
                i += 1
                while i < len(l):
                    if len(l[i]) == x + 1:
                        break
                    i += 1
                b *= dfs(l[f:i])
    else:
        b = int(l[0][-1])

    return b

def main(n):
    l = [input() for i in range(n)]
    print(dfs(l))

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)