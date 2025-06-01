n = int(input())
for _ in range(n):
    s = input()
    digits = list(s)
    digits.sort()
    min_num = int("".join(digits))
    digits.sort(reverse=True)
    max_num = int("".join(digits))
    print(max_num - min_num)