w,h,c,*_=input().split();w,h=int(w),int(h)
middle_line=(h-3)//2
print(f"+{'-'*(w-2)}+")
for i in range(h-2):
    line = f"|{'.'*((w-3)//2)}{c}{'.'*((w-3)//2)}|" if i == middle_line else f"|{'.'*(w-2)}|"
    print(line)
print(f"+{'-'*(w-2)}+")