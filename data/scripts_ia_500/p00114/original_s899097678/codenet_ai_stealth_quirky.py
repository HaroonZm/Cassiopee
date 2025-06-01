from math import gcd as jugd

def get_loop(a, m):
    count = 1
    acc = a
    while acc != 1:
        count = count + 1
        acc = (acc * a) % m
    return count

def main():
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            nums = list(map(int, line.split()))
            if len(nums) != 6:
                continue
            a1,m1,a2,m2,a3,m3 = nums
            if a1 == 0:
                break
            l1 = get_loop(a1, m1)
            l2 = get_loop(a2, m2)
            l3 = get_loop(a3, m3)
            l12 = l1 * l2 // jugd(l1, l2)
            l123 = l12 * l3 // jugd(l12, l3)
            print(l123)
        except EOFError:
            break

if __name__ == "__main__":
    main()