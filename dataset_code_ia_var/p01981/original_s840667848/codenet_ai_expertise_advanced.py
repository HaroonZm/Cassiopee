from sys import stdin

for line in stdin:
    a = line.strip().split()
    if not a or a[0] == "#":
        break
    name, n1, *rest = a
    n1 = int(n1)
    n2 = int(rest[0]) if rest else 0
    match n1, n2:
        case n1, _ if n1 <= 30:
            print(line.strip())
        case 31, n2 if n2 <= 4:
            print(line.strip())
        case _:
            a[0] = "?"
            a[1] = str(n1 - 30)
            print(" ".join(a))