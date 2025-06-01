m, f, b = map(int, input().split())
print('NA' if m + f < b else '0' if m > b else b - m)