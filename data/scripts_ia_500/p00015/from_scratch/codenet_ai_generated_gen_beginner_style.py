N = int(input())
for _ in range(N):
    a = input().strip()
    b = input().strip()
    if len(a) > 80 or len(b) > 80:
        print("overflow")
        continue
    sum_int = int(a) + int(b)
    sum_str = str(sum_int)
    if len(sum_str) > 80:
        print("overflow")
    else:
        print(sum_str)