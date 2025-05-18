import sys

def main() -> None:
    n = int(next_str())
    s = next_str()
    t = next_str()

    ans = n
    for i in range(n):
        flg = False
        for j in range(n - i):
            if s[i + j] != t[j]:
                ans += 1
                flg = True
                break
        if not flg: break
    print(ans)

def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result

if __name__ == '__main__':
    main()