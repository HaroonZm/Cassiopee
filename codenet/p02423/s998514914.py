x = int(input())

BITMASK = (1 << 32) - 1

print("{:032b}".format(x))
print("{:032b}".format(~x & BITMASK))
print("{:032b}".format((x << 1) & BITMASK))
print("{:032b}".format((x >> 1) & BITMASK))