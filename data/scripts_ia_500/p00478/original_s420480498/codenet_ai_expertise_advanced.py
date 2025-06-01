m = input()
n = int(input())
x = [input() for _ in range(n)]

count = sum(m in (s := seq + seq[:11]) for seq in x)
print(count)