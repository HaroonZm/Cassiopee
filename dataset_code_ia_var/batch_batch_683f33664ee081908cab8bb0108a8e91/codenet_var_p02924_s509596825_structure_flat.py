n = int(input())
if n % 2 == 0:
    even = n
    odd = n - 1
else:
    even = n - 1
    odd = n
even_2 = int(even / 2)
result = even_2 * odd
print(result)