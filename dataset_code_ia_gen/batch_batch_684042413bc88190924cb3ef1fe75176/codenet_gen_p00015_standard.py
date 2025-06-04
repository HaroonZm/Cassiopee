n=int(input())
for _ in range(n):
    a=input().lstrip('0') or '0'
    b=input().lstrip('0') or '0'
    if len(a)>80 or len(b)>80:
        print("overflow")
        continue
    s=str(int(a)+int(b))
    print(s if len(s)<=80 else "overflow")