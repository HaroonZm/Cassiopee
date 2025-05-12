def shred(num, bit):
    num = list(str(num))
    i = 0
    while bit:
        if bit & 1:
            num[i] += num.pop(i+1)
        else:
            i += 1

        bit >>= 1

    return num

def testcase_ends():
    t, num = map(int, raw_input().split())
    if t == 0 and num == 0:
        return 1

    cutcand = []
    curmax = -1
    for i in range(1<<(len(str(num))-1)):
        cut = shred(num, i)
        sumcut = sum(map(int, cut))

        if sumcut > t:
            continue
        elif sumcut == curmax:
            cutcand.append(cut)
        elif sumcut > curmax:
            cutcand = [cut]
            curmax = sumcut
    
    if len(cutcand) > 1:
        print 'rejected'
    elif len(cutcand) == 1:
        print curmax, ' '.join(cutcand[0])
    else:
        print 'error'

    return 0

def main():
    while True:
        if testcase_ends():
            return 0

if __name__ == '__main__':
    main()