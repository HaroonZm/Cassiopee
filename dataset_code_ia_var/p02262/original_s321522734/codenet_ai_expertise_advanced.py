import sys
from itertools import count

def insertion_sort(nums, n, gap):
    cnt = 0
    for i in range(gap, n):
        v = nums[i]
        j = i
        while j >= gap and nums[j-gap] > v:
            nums[j] = nums[j-gap]
            j -= gap
            cnt += 1
        nums[j] = v
    return cnt

def shell_sort(nums):
    n = len(nums)
    # Generate gaps using 3x+1 sequence, optimized with itertools
    gaps = [g for g in (3**k for k in count()) if g <= n]
    gaps.reverse()
    print(len(gaps))
    print(' '.join(map(str, gaps)))
    cnt = sum(insertion_sort(nums, n, gap) for gap in gaps)
    print(cnt)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    shell_sort(nums)
    print('\n'.join(map(str, nums)))