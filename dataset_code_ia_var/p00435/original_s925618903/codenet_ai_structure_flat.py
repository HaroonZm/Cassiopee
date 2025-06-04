s = input().strip()
w = -3
base = "A"
alphabet = 26
b = ord(base)

result = s
result = map(ord, result)
result = map(lambda x: x - b, result)
result = map(lambda x: (x + alphabet + w) % alphabet, result)
result = map(lambda x: x + b, result)
result = map(chr, result)
result = "".join(result)

print(result)