continue_program = True

while continue_program:
    n = int(raw_input())
    if n == 0:
        continue_program = False
        break

    exist = set()
    time = [0] * 1000
    bless = [0] * 1000

    for i in range(n):
        md, hm, io, p = raw_input().split()
        h, m = map(int, hm.split(":"))
        t = 60 * h + m
        p = int(p)

        if io == "I":
            time[p] = t
            exist.add(p)
        else:
            if p in exist:
                exist.remove(p)
            if p == 0:
                for i in exist:
                    if time[p] > time[i]:
                        bless[i] += t - time[p]
                    else:
                        bless[i] += t - time[i]
            elif 0 in exist:
                if time[0] > time[p]:
                    bless[p] += t - time[0]
                else:
                    bless[p] += t - time[p]

    print(max(bless))