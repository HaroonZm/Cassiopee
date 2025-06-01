def main():
    while True:
        try:
            n = int(raw_input())
        except:
            break
        if n == 0:
            break
        ar = raw_input() + ' '
        i = 0
        while i < n:
            cnt = 1
            tmp = list()
            j = 0
            while j < len(ar)-1:
                if ar[j] == ar[j+1]:
                    cnt += 1
                else:
                    tmp.append(str(cnt))
                    tmp.append(ar[j])
                    cnt = 1
                j += 1
            ar = ''.join(tmp) + ' '
            i += 1
        print ar.rstrip()

main()