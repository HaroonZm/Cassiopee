def main():
    n, m = map(int, input().split())
    left = 1
    right = n

    for _ in range(m):
        left_i, right_i = map(int, input().split())
        left = max(left, left_i)
        right = min(right, right_i)
    
    print(max(0, right - left + 1))

main()