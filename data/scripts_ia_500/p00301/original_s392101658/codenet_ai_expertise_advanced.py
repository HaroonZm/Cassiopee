w = int(input())
offset = (3 ** 0 - 1) // 2  # initial offset (0)
chars = '0+-'
result = []

for n in range(30):  # large enough upper bound to cover w
    index = (w + (3 ** n - 1) // 2) // (3 ** n) % 3
    result.append(chars[index])
    if w <= (3 ** n - 1) // 2:
        break

print(''.join(result[::-1]))