n = int(input())

ans = float('inf')
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        x = max(len(str(i)), len(str(n // i)))
        ans = min(ans, x)
        
print(ans)