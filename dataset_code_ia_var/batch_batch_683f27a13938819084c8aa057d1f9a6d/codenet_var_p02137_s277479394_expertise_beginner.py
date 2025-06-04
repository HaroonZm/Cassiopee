p = int(input())
total = 0

if p >= 10000:
    num = p // 10000
    total = total + num * 10000
    p = p - num * 10000

if p >= 5000:
    num = p // 5000
    total = total + num * 5000
    p = p - num * 5000

if p >= 1000:
    num = p // 1000
    total = total + num * 1000
    p = p - num * 1000

if p >= 500:
    num = p // 500
    total = total + num * 500
    p = p - num * 500

print(total)