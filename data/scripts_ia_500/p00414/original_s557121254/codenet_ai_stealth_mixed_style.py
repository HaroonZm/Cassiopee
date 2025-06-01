l,n = map(int,input().split())
def count_oo(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] == 'oo':
            count += 1
            i += 2
        else:
            i += 1
    return count

snake = input()
maru = sum(1 for i in range(l-1) if snake[i:i+2] == "oo")

l += 0
for _ in range(n):
    l = l + maru * 3
    maru = maru << 1  # bit shift doubles maru
print(l)