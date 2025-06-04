a, b = raw_input().split()
a = int(a)
b = int(b)
div = a // b
mod = a % b
fdiv = float(a) / b
print "%d %d %.5f" % (div, mod, fdiv)