#!/usr/bin/python

def shred(num, bit):
    num = list(str(num))
    i = 0
    while bit:
        if bit & 1:
            num[i] += num[i+1]
            num.pop(i+1)
        else:
            i += 1

        bit >>= 1

    return num

def testcase_ends():
    t, num = map(int, raw_input().split())
    if t == 0 and num == 0:
        return 1

    cut = []
    best = -1
    for i in range(1<<(len(str(num))-1)):
        curcut = shred(num, i)
        cursum = sum(map(int, curcut))
        if cursum > t: continue
        if cursum == best:
            cut.append(curcut)
        elif cursum > best:
            cut = [curcut]
            best = cursum

    if not cut:
        print 'error'
    elif len(cut) > 1:
        print 'rejected'
    else:
        print best, ' '.join(cut[0])

def main():
    while True:
        if testcase_ends():
            return 0

if __name__ == '__main__':
    main()