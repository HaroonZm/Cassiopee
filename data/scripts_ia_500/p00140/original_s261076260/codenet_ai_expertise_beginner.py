n = int(input())

for i in range(n):
    start, end = input().split()
    start = int(start)
    end = int(end)

    anslist = []

    if start <= 5:
        if start > end:
            i = start
            while i >= end:
                anslist.append(i)
                i = i - 1
        else:
            i = start
            while i <= end:
                anslist.append(i)
                i = i + 1
    elif start < end:
        i = start
        while i <= end:
            anslist.append(i)
            i = i + 1
    else:
        i = start
        while i < 10:
            anslist.append(i)
            i = i + 1

        if end <= 5:
            i = 5
            while i >= end:
                anslist.append(i)
                i = i - 1
        else:
            i = 5
            while i > 0:
                anslist.append(i)
                i = i - 1
            i = 0
            while i <= end:
                anslist.append(i)
                i = i + 1

    out = ""
    for ans in anslist:
        out = out + str(ans) + " "
    print(out.strip())