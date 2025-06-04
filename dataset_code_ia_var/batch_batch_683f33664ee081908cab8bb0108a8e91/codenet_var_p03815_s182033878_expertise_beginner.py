N = int(input())

ans = (N // 11) * 2
mod = N % 11

if mod == 0:
    result = ans
elif mod <= 6:
    result = ans + 1
else:
    result = ans + 2

print(result)