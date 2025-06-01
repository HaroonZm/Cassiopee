if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    for line in iter(input, ''):
        L, R = map(int, line.split())
        if L == R == 0:
            break

        arr = {0}
        if L:
            arr.update(map(int, input().split()))
        if R:
            arr.update(map(int, input().split()))

        arr = sorted(arr)
        print(max(b - a for a, b in zip(arr, arr[1:])))