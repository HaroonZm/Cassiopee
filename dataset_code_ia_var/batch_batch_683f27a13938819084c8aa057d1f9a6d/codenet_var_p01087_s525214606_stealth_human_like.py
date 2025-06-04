import sys
input = sys.stdin.readline

def calc(i, lvl, fs, limit):
    # hmm, maybe I could rename fs, but let's keep it for now
    # lvl means level/depth I guess
    if fs[i][1] not in ['+', '*']:
        return i, int(fs[i][1])
    if fs[i][1] == '+':
        res = 0
        j = i + 1
        while j < limit:
            if fs[j][0] <= lvl:
                break
            # let's check if it's an operator
            if fs[j][1] == '+' or fs[j][1] == '*':
                j, val = calc(j, lvl + 1, fs, limit)
                res += val
            else:
                res += int(fs[j][1])
            j += 1
        return j-1, res
    elif fs[i][1] == '*':
        prod = 1
        j = i + 1
        while j < limit:
            if fs[j][0] <= lvl:
                break
            if fs[j][1] in ['+', '*']:
                j, v2 = calc(j, lvl+1, fs, limit)
                prod *= v2
            else:
                prod *= int(fs[j][1])
            j += 1
        return j-1, prod
    # no else needed, we covered all, I think

def main():
    # feels like we could process multiple cases this way
    while True:
        n = int(input())
        if n == 0:
            break
        fs = []
        for _ in range(n):
            tmp = input().rstrip()
            lvl = tmp.count('.')
            val = tmp.replace('.', '')
            fs.append([lvl, val])
        _, res = calc(0, 0, fs, len(fs))
        print(res)
        # that's it I guess

if __name__ == "__main__":
    main()