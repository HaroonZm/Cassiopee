from sys import stdin, exit

N = int(stdin.readline())
for _ in range(N):
    if int(stdin.readline()) & 1:
        print('first')
        exit()
print('second')