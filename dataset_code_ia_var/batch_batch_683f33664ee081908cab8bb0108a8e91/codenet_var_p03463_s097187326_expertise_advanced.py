n, a, b = map(int, input().split())
print(("Alice", "Borys")[(a - b - 1) % 2 == 0])