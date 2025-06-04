while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far)