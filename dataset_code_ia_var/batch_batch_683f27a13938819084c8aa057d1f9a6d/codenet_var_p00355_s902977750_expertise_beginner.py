def main():
    a_b = input().split()
    a = int(a_b[0])
    b = int(a_b[1])

    n = int(input())
    s = []
    f = []
    i = 0
    while i < n:
        temp = input().split()
        s.append(int(temp[0]))
        f.append(int(temp[1]))
        i += 1

    i = 0
    while i < n:
        if not (f[i] <= a or b <= s[i]):
            return 1
        i += 1
    return 0

if __name__ == '__main__':
    print(main())