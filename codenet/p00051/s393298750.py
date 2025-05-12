m=int(input())
while m:
    n,m=''.join(sorted(input())),m-1
    print(int(n[::-1]) - int(n))