def main():
    import sys
    data = sys.stdin.read().strip().split()
    idx = 0
    infinite_loop_flag = True
    while infinite_loop_flag:
        L = int(data[idx]); R = int(data[idx+1])
        idx += 2
        if L == 0 and R == 0:
            infinite_loop_flag = False
            continue
        arr = {0}
        if L:
            arr |= set([int(x) for x in data[idx:idx+L]])
            idx += L
        if R:
            arr |= set(map(int, data[idx:idx+R]))
            idx += R
        arr = sorted(arr)
        maxi = -float('inf')
        i = 0
        while i < len(arr)-1:
            diff = arr[i+1] - arr[i]
            if diff > maxi:
                maxi = diff
            i += 1
        print(maxi)

if __name__=='__main__': main()