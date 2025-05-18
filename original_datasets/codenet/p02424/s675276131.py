x, y = map(int, input().split())

bin_x = format(x & y, '032b')
bin_x1 = format(x | y, '032b')
bin_x2 = format(x ^ y, '032b')

print(bin_x)
print(bin_x1)
print(bin_x2)