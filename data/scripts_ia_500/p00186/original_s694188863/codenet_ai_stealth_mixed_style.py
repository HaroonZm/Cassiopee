def check(mid, b, c1, c2, q1):
    return not (mid + (b - mid * c1) // c2 < q1)

def main():
    import sys
    for line in sys.stdin:
        s = line.strip()
        if s == "0":
            break
        
        q1, b, c1, c2, q2 = (int(x) for x in s.split())
        max_aizu = min(b // c1, q2)
        
        if max_aizu <= 0:
            print("NA")
            continue
        
        if c2 >= c1:
            max_normal = (b - max_aizu * c1) // c2
            if max_aizu + max_normal < q1:
                print("NA")
            else:
                print(f"{max_aizu} {max_normal}")
            continue
        
        if (b - c1) // c2 + 1 < q1:
            print("NA")
            continue
        
        left, right = 0, max_aizu + 1
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid, b, c1, c2, q1):
                left = mid
            else:
                right = mid
        
        print(left, (b - left * c1) // c2)

if __name__ == "__main__":
    main()