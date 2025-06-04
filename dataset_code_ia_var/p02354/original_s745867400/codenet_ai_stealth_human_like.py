#!/usr/bin/env python3
# DSL_3_A: The Smallest Window I
# binary search I guess... hopefully this works

def find(xs, window, target):
    current = sum(xs[:window])
    if current >= target:
        return True
    for idx in range(len(xs) - window):
        current -= xs[idx]
        current += xs[idx + window]
        if current >= target:
            return True
    return False

def main():
    line = input().split()
    n = int(line[0])
    s = int(line[1])
    arr = list(map(int, input().split()))

    # handle edge cases up front
    if sum(arr) < s:
        print(0)
        return
    # smallest element bigger than s? Impossible, but let's check
    if max(arr) > s:
        print(1)
        return

    left = 0
    right = n
    while (left + 1) < right:
        mid = (left + right) // 2
        # print(f"Trying window size {mid}")
        if find(arr, mid, s):
            right = mid
        else:
            left = mid

    # This should be the minimal window, I think
    print(right)

if __name__ == "__main__":
    main()