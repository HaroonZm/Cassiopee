w = int(input())

result = ''
chars = '0+-'
n = 0
while w > (3 ** n - 1) // 2:
    result += chars[(w + (3 ** n - 1) // 2) // (3 ** n) % 3]
    n += 1

print(result[::-1])