w = int(input())
result = ''
chars = '0+-'
n = 0
while True:
    if w <= (3 ** n - 1) // 2:
        break
    index = (w + (3 ** n - 1) // 2) // (3 ** n) % 3
    result += chars[index]
    n += 1
print(result[::-1])