from sys import stdin, exit

get_input = lambda: stdin.readline().strip()
chars = []
for ch in get_input():
    chars.append(ch)

def do_pop(lst, cnt=1):
    while cnt:
        lst.pop()
        cnt -= 1

lens = len(chars)
if not lens % 2:
    do_pop(chars, 2)
else:
    chars.pop()

half = int(len(chars)/2)
if chars[:half] == chars[half:]:
    print(len(chars))
    exit()

# procedural functional for loop with while
i = 0
while i < len(chars)//2:
    [chars.pop() for _ in (0,1)]  # listcomp used as statement
    half = len(chars)//2
    if (lambda x: x)(chars[:half]) == chars[half:]:
        print(len(chars))
        exit()
    i += 1