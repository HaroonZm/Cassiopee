while True:
    n = input()
    if n==0: break
    s = raw_input()
    ba = 0; p = [0]*n
    for i in range(100):
        if s[i] == 'M':
            p[i%n] += 1
        elif s[i] == 'L':
            p[i%n] += ba+1; ba=0;
        else:
            ba += p[i%n]+1; p[i%n]=0;
    print " ".join(map(str, sorted(p))), str(ba)