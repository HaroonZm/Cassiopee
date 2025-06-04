import sys

chklist = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

word = ''
for i in sys.stdin:
    word += i

for n in chklist:
    cnt = 0
    for w in word:
        if n.upper() == w.upper():
            cnt += 1
    print('{} : {}'.format(n, cnt))