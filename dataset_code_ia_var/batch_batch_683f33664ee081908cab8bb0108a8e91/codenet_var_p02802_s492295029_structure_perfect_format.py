def main():
    N, M = map(int, input().split())
    ac = [0 for _ in range(N)]
    wa = [0 for _ in range(N)]
    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    for i in range(N):
        if ac[i] == 0:
            wa[i] = 0
    print(str(sum(ac)) + " " + str(sum(wa)))

if __name__ == '__main__':
    main()