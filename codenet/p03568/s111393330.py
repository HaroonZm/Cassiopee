n = int(input())
a = list(map(int, input().split()))
even_count = 0
for i in range(n):
  if a[i]%2 == 0:
    even_count += 1
print(3**n-(2**even_count))