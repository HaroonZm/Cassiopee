bit = int(input())
print(f"0:")
d = 1
while d < 2 ** bit:
    print(f"{d}: ", end="")
    elems = []
    elem = 0
    while elem < bit:
        if d & (1 << elem):
            elems.append(str(elem))
        elem += 1
    print(" ".join(elems))
    d += 1