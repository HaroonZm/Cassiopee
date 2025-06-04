import sys

def main():
    s = input()
    s = list(s)
    ans = 0
    a = 0
    cur = 0

    while cur < len(s) - 2:
        if s[cur] == "A" and s[cur+1] == "B" and s[cur+2] == "C":
            ans += a + 1
            cur += 2
            s[cur] = "A"
        else:
            if s[cur] == "A":
                a += 1
            else:
                a = 0
            cur += 1

    print(ans)

if __name__ == "__main__":
    main()