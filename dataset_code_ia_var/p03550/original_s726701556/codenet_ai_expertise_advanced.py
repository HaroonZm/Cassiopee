from operator import itemgetter

n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

match n:
    case 1:
        print(abs(arr[0] - b))
    case _:
        print(max(map(abs, (arr[-1] - b, arr[-1] - arr[-2]))))