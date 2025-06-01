a_count = 0
b_count = 0
ab_count = 0
o_count = 0

while True:
    try:
        line = input()
        if not line:
            break
        parts = line.split(",")
        if len(parts) != 2:
            continue
        number = parts[0]
        blood = parts[1]
        if blood == "A":
            a_count += 1
        elif blood == "B":
            b_count += 1
        elif blood == "AB":
            ab_count += 1
        elif blood == "O":
            o_count += 1
    except EOFError:
        break

print(a_count)
print(b_count)
print(ab_count)
print(o_count)