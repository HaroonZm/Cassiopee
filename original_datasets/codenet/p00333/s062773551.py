def sdk(a,b):
    if a < b:
        a,b = b,a
    if a%b == 0:
        return b
    else:
        return sdk(b, a%b)

w,h,c=map(int, input().split())
t = sdk(w,h)
print(w//t * h//t * c)