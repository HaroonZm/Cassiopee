from sys import stdin

def min_operations(*nums):
    a, b, c = sorted(nums)
    cnt1 = c - b
    diff = c - (a + cnt1)
    cnt2, rem = divmod(diff, 2)
    return cnt1 + cnt2 + (rem * 2 - rem)

if __name__ == "__main__":
    print(min_operations(*map(int, stdin.readline().split())))