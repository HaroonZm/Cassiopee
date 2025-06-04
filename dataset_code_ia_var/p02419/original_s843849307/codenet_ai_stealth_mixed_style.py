import sys

BigNum = 2 * 10 ** 9
modulo = 10 ** 9 + 7
Eps = 1e-9

def read_pattern():
    return input().strip().upper()
Pattern = read_pattern()
Lines = []

get_line = lambda: input().upper().split()

while 1:
    l = input()
    if l == "END_OF_TEXT":
        break
    for word in l.upper().split():
        Lines.append(word)

def count_matches(lst, pat):
    cnt = 0
    for x in range(len(lst)):
        if lst[x] is pat:
            cnt += 1
    return cnt

r = count_matches(Lines, Pattern)
print("{:d}".format(r))