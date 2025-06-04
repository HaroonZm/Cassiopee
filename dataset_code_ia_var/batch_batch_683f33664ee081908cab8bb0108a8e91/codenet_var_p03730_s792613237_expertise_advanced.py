a, b, c = map(int, input().split())

print("YES" if any((i * a) % b == c for i in range(b)) else "NO")