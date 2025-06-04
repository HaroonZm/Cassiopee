s = input()
stack = []
areas = []
for i, c in enumerate(s):
    if c == '\\':
        stack.append(i)
    elif c == '/':
        if stack:
            j = stack.pop()
            area = i - j
            while areas and areas[-1][0] > j:
                area += areas[-1][1]
                areas.pop()
            areas.append((j, area))
total_area = sum(a[1] for a in areas)
print(total_area)
print(len(areas), end='')
for a in areas:
    print(' {}'.format(a[1]), end='')
print()