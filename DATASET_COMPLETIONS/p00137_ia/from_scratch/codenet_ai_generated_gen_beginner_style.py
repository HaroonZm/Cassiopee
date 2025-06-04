d = int(input())
n = 4

for case_num in range(1, d+1):
    s = int(input())
    print("Case {}:".format(case_num))
    for _ in range(10):
        square = s * s
        square_str = str(square).zfill(2 * n)
        start = (len(square_str) - n) // 2
        s = int(square_str[start:start + n])
        print(s)