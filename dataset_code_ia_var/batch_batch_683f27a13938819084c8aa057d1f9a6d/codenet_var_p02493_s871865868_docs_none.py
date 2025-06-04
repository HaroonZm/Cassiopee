n = int(raw_input())
if n <= 100:
    l = map(int, raw_input().split(' '))
    print ' '.join(map(str, l[::-1]))