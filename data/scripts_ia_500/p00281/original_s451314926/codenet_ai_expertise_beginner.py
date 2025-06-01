def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    works = []
    for i in range(n + 1):
        works.append([])
    while True:
        s, t, e = input().split()
        s = int(s)
        if s == 0:
            break
        t = int(t)
        e = int(e)
        works[s].append((t - 1, e))
    l = int(input())
    for _ in range(l):
        blst_str = input().split()
        blst = []
        for val in blst_str:
            blst.append(int(val))
        for i in range(1, n + 1):
            total = 0
            for t, e in works[i]:
                total += blst[t] * e
            print(total, end=" ")
        print()
main()