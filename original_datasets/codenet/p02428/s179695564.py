n = int(input())
nn = pow(2, n)

k = list(map(int, input().split()))
mask = k[1:k[0]+1]

if k[0] == 0:
    for i in range(nn):
        if i == 0:
            print("0:")
        else:
            bin_str = "0" + str(n) + "b"
            bin_i = format(i, bin_str)
            ilist = list(bin_i)
            tmplist = []
            for j, bini in enumerate(ilist):
                if bini == '1':
                    tmplist.append(n - j - 1)
            tmplist.sort()
            tmp_str = ' '.join(str(tmp) for tmp in tmplist)
            print(str(i) + ": " + tmp_str)

else:
    for i in range(nn):
        if i == 0:
            continue
        bin_str = "0" + str(n) + "b"
        bin_i = format(i, bin_str)
        ilist = list(bin_i)
        tmplist = []
        for j, bini in enumerate(ilist):
            if bini == '1':
                tmplist.append(n - j - 1)
        if len(set(mask) & set(tmplist)) == k[0]:
            tmplist.sort()
            tmp_str = ' '.join(str(tmp) for tmp in tmplist)
            print(str(i) + ": " + tmp_str)