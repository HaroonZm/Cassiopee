import sys
sys.setrecursionlimit(100000)
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 1e-9

def binary_search(need, budget, aizu, normal, limit):
    left, right = 1, limit
    num_aizu, num_normal = 0, 0
    while left <= right:
        mid = (left + right) // 2
        rest = budget - mid * aizu
        if rest >= 0 and mid + (rest // normal) >= need:
            num_aizu = mid
            num_normal = rest // normal
            left = mid + 1
        else:
            right = mid - 1
    return num_aizu, num_normal

def main():
    while True:
        data = input()
        if data == "0":
            break
        need, budget, aizu, normal, limit = map(int, data.split())
        result = binary_search(need, budget, aizu, normal, limit)
        if result[0] == 0:
            print("NA")
        else:
            print("{} {}".format(*result))

if __name__ == "__main__":
    main()