n=0
while True:
    try:
        s=str(input())
        if s==s[::-1]:
            n+=1
    except:
        break
print(n)