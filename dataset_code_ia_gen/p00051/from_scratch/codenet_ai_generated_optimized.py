n=int(input())
for _ in range(n):
    s=input()
    max_num=int(''.join(sorted(s,reverse=True)))
    min_num=int(''.join(sorted(s)))
    print(max_num - min_num)