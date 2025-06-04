def main():
    from operator import itemgetter

    repeat = True
    while repeat:
        try:
            n = int(input())
        except:
            break
        if not n:
            repeat = False
            continue

        arr, i = [], 0
        # Procédural et liste en compréhension partielle
        while i < n:
            s = input().split()
            x = int(s[0])
            ts = [int(q) for q in s[1:]]
            t = 0
            j = 0
            # Style C-like
            while j < 4:
                a = ts[j*2]*60 + ts[j*2+1]
                t = t + a
                j += 1
            arr.append([x, t])
            i += 1

        # Style fonctionnel mélangé
        arr.sort(key=itemgetter(1))
        for idx in (0,1,-2):
            print(arr[idx][0])

main()