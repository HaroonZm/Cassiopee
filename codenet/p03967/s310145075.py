import sys

def slove():
    input = sys.stdin.readline
    s = str(input().rstrip('\n'))
    g = 0
    p = 0
    for i in range(len(s)):
        if s[i] == "g":
            g += 1
        else:
            p += 1
    pp = len(s) // 2
    cnt = 0
    for i in range(len(s)):
        if pp != 0:
            pp -= 1
            if s[i] == "g":
                cnt += 1
        else:
            if s[i] == "p":
                cnt -= 1
    print(cnt)

if __name__ == '__main__':
    slove()