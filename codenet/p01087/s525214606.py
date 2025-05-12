import sys
input = sys.stdin.readline

def calc(i, level, fs, lim):
    if fs[i][1] not in "+*":
        return i, int(fs[i][1])
    if fs[i][1] == "+":
        tmp = 0
        j = i+1
        while j < lim:
            if fs[j][0] <= level:
                break
            if fs[j][1] in "*+":
                j, tmp2 = calc(j, level+1, fs, lim)
                tmp += tmp2
            else:
                tmp += int(fs[j][1])
            j += 1
        return j-1, tmp
    elif fs[i][1] == "*":
        tmp = 1
        j = i+1
        while j < lim:
            if fs[j][0] <= level:
                break
            if fs[j][1] in "*+":
                j, tmp2 = calc(j, level+1, fs, lim)
                tmp *= tmp2
            else:
                tmp *= int(fs[j][1])
            j += 1
        return j-1, tmp

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        fs = [[0,0] for i in range(n)]

        for i in range(n):
            tmp = input().strip()
            fs[i][0] = tmp.count(".")
            fs[i][1] = tmp.replace(".", "")
        _, ans = calc(0, 0, fs, len(fs))
        print(ans)

if __name__ == "__main__":
    main()