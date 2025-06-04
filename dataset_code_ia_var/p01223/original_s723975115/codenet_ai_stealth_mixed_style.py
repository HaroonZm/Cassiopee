import sys

def main():
    import functools
    readline = sys.stdin.readline
    T = int(readline())
    count = 0
    while True:
        if count >= T: break
        n = int(readline())
        # mélange avec une compréhension et boucle classique
        a = list(map(int, readline().split()))
        result = [0, 0]
        i = 1
        while i < n:
            diff1 = a[i] - a[i-1]
            diff2 = a[i-1] - a[i]
            if diff1 > result[0]:
                result[0] = diff1
            if diff2 > result[1]:
                result[1] = diff2
            i += 1
        print(result[0], end=' ')
        print("{}".format(result[1]))
        count += 1

main()