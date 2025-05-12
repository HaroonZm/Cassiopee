s=0
while True:
    try:
        i=input()
        if i==i[::-1]:
            s+=1
    except:
        break
print(s)