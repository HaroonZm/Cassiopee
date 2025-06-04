def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    a1 = 12.5 * a
    a2 = 12.5 * (a + 1)
    b1 = 10 * b
    b2 = 10 * (b + 1)
    if a2 <= b1:
        print(-1)
        return
    if b2 <= a1:
        print(-1)
        return
    if a1 > b1:
        ans = int(a1+1) if a1 != int(a1) else int(a1)
    else:
        ans = b1
    print(ans)
main()