import sys

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

P = str(input()).upper()
line = []

while True:
    tmp_line = str(input())
    if tmp_line == 'END_OF_TEXT':
        break
    line += tmp_line.upper().split()

ans = 0

for tmp_word in line:
    if tmp_word == P:
        ans += 1

print("%d"%(ans))