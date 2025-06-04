n = int(input())
minsum = float("inf")
i = 0
while i < n-1:
    cnt = 0
    a = i+1
    b = n-i-1
    def digit_sum(val):
        return sum(map(int, list(str(val))))
    for x in [a,b]:
        digits = list(str(x))
        for d in digits:
            cnt += int(d)
    alt_sum = digit_sum(a) + digit_sum(b)
    if min(cnt, alt_sum) < minsum:
        minsum = min(cnt, alt_sum)
    i += 1
print(minsum)