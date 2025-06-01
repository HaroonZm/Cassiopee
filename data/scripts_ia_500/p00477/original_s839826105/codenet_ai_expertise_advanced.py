from sys import stdin

total_seconds = sum(int(stdin.readline()) for _ in range(4))
minutes, seconds = divmod(total_seconds, 60)

print(minutes, seconds, sep='\n')