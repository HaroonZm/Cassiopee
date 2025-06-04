A, B, C = input().split()
mod = 1000000007

count = 0
start = int(A)
end = int(B)
needle = C

for num in range(start, end + 1):
    s = str(num)
    idx = 0
    while True:
        idx = s.find(needle, idx)
        if idx == -1:
            break
        count += 1
        idx += 1

print(count % mod)