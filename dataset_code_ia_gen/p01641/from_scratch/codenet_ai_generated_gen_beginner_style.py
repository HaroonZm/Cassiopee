s = input()

code = ""
prev = 0
for c in s:
    ascii_val = ord(c)
    diff = ascii_val - prev
    if diff > 0:
        code += "+" * diff
    elif diff < 0:
        code += "-" * (-diff)
    code += "."
    prev = ascii_val

print(code)