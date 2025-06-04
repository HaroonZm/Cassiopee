from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    for i in range(1, m - 1):
        if a[i] & 1:
            if a[0] & 1:
                if a[-1] & 1:
                    print("Impossible")
                    return
                a[i], a[-1] = a[-1], a[i]
            else:
                a[i], a[0] = a[0], a[i]

    print(*a)
    if m == 1:
        if a[0] > 1:
            a[0] -= 1
            a.append(1)
            print(m + 1)
        else:
            print(m)
    else:
        if a[-1] == 1:
            print(m - 1)
            a.pop()
            a[0] += 1
        else:
            print(m)
            a[0] += 1
            a[-1] -= 1
    print(*a)

if __name__ == "__main__":
    main()