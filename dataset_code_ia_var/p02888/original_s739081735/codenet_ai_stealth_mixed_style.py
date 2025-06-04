import bisect

def main():
    N = int(input())
    arr = [int(x) for x in input().split()]
    arr = sorted(arr)

    answer = 0
    idx = 0
    while idx < N-1:
        for j in range(idx+1, N):
            tmp = bisect.bisect_left(arr, arr[idx]+arr[j]) - (j+1)
            answer = answer + tmp
        idx += 1

    print(answer)

if __name__ == '__main__':
    main()